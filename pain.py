from fastapi import FastAPI, HTTPException
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Database Configuration
DATABASE_URL = "postgresql://user:password@localhost/taskdb"
database = Database(DATABASE_URL)
metadata = MetaData()

# Task Table Definition
tasks = Table(
    "tasks", metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(200)),
    Column("priority", Integer)
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# AI Model Setup
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# FastAPI App Instance
app = FastAPI()

# Pydantic Models
class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: int

class GenerateTasksRequest(BaseModel):
    prompt: str

# Startup & Shutdown Events
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Backend API is running!"}

@app.get("/tasks/")
async def get_tasks():
    query = select(tasks)
    return await database.fetch_all(query)

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/")
async def create_task(task: Task):
    query = tasks.insert().values(
        id=task.id,
        title=task.title,
        description=task.description,
        priority=task.priority
    )
    await database.execute(query)
    return {"message": "Task added successfully"}

@app.post("/generate-tasks/")
async def generate_tasks(request: GenerateTasksRequest):
    try:
        inputs = tokenizer(request.prompt, return_tensors="pt")
        outputs = model.generate(**inputs)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        task_list = generated_text.split("; ")
        task_list = [task.strip() for task in task_list if task.strip()]

        return {"tasks": task_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating tasks: {str(e)}")

@app.post("/generate-and-create-tasks/")
async def generate_and_create_tasks(request: GenerateTasksRequest):
    try:
        generated_tasks = await generate_tasks(request)
        task_list = generated_tasks["tasks"]

        for i, task_title in enumerate(task_list):
            task = Task(
                id=i + 1,
                title=task_title,
                description=f"Automatically generated task: {task_title}",
                priority=1
            )
            await create_task(task)

        return {"message": f"{len(task_list)} tasks generated and created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating and creating tasks: {str(e)}")
