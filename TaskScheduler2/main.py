from fastapi import FastAPI  # Import FastAPI to create the web API
from databases import Database  # Import Database to manage async database operations
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String  # SQLAlchemy for database setup
from sqlalchemy.sql import select  # Used to select data from the database
from pydantic import BaseModel  # Pydantic for data validation and request body parsing
from transformers import pipeline

# Load a text-to-text model from Hugging Face (T5 is good for this)
task_generation_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")


# Define the SQLite database URL
DATABASE_URL = "sqlite:///./tasks.db"

# Create a Database object to handle DB operations
database = Database(DATABASE_URL)
# Metadata object to hold information about tables
metadata = MetaData()

# Define the 'tasks' table with columns: id, title, description, priority
tasks = Table(
    "tasks", metadata,
    Column("id", Integer, primary_key=True),  # Unique ID for each task
    Column("title", String(100)),  # Title of the task
    Column("description", String(200)),  # Task description
    Column("priority", Integer)  # Priority level of the task
)

# Create a database engine and generate the tasks table
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Create an instance of FastAPI
app = FastAPI()

# Pydantic model for task data validation
class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: int

# Connect to the database when the app starts
@app.on_event("startup")
async def startup():
    await database.connect()

# Disconnect from the database when the app shuts down
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Root endpoint to confirm the API and DB connection
@app.get("/")
async def read_root():
    return {"message": "Database connected successfully!"}



# Get all tasks from the database
@app.get("/tasks/")
async def get_tasks():
    query = select(tasks)
    return await database.fetch_all(query)

# Get a specific task by its ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task:
        return task
    return {"error": "Task not found"}

# Update an existing task by its ID
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    query = tasks.update().where(tasks.c.id == task_id).values(title=task.title, description=task.description, priority=task.priority)
    await database.execute(query)
    return {"message": "Task updated successfully"}

# Delete a task by its ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": "Task deleted successfully"}

# Create a new task
@app.post("/tasks/")
async def create_task(task: Task):
    # Insert a new task into the database
    query = tasks.insert().values(
        id=task.id,
        title=task.title,
        description=task.description,
        priority=task.priority
    )
    await database.execute(query)  # Execute the insert query
    return {"message": "Task added successfully"}


@app.post("/generate-tasks/")
async def generate_tasks(prompt: str):
    # Send the user prompt to the model and get generated text
    result = task_generation_pipeline(f"Turn this into tasks: {prompt}")

    # The model response comes back as a list — we take the first result
    generated_tasks = result[0]["generated_text"]

    return {"tasks": generated_tasks}

