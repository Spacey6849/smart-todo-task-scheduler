from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import networkx as nx
from datetime import datetime
import openai

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

tasks_graph = nx.DiGraph()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: int
    deadline: datetime
    dependencies: List[int] = []
    completed: bool = False

# In-memory task store
tasks = {}

@app.post("/tasks/")
def create_task(task: Task):
    if task.id in tasks:
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks[task.id] = task
    tasks_graph.add_node(task.id, **task.dict())
    for dep in task.dependencies:
        if dep not in tasks:
            raise HTTPException(status_code=400, detail=f"Dependency task {dep} not found")
        tasks_graph.add_edge(dep, task.id)
    return task

@app.get("/tasks/")
def get_tasks():
    return list(tasks.values())

@app.get("/schedule/")
def get_schedule():
    try:
        sorted_tasks = list(nx.topological_sort(tasks_graph))
        sorted_tasks = sorted(sorted_tasks, key=lambda t: (tasks[t].completed, tasks[t].deadline, -tasks[t].priority))
        return [tasks[t] for t in sorted_tasks]
    except nx.NetworkXUnfeasible:
        raise HTTPException(status_code=400, detail="Circular dependency detected")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    tasks_graph.add_node(task.id, **task.dict())
    for dep in task.dependencies:
        if dep not in tasks:
            raise HTTPException(status_code=400, detail=f"Dependency task {dep} not found")
        tasks_graph.add_edge(dep, task.id)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    tasks_graph.remove_node(task_id)
    return {"detail": "Task deleted"}

@app.post("/generate-tasks/")
def generate_tasks(prompt: str):
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who breaks down projects into clear, actionable tasks."},
                {"role": "user", "content": f"Break this project into clear, actionable tasks: {prompt}"}
            ],
            max_tokens=500
        )
        task_descriptions = response.choices[0].message.content.strip().split("\n")
        generated_tasks = []
        for idx, desc in enumerate(task_descriptions):
            if not desc.strip() or not "." in desc:
                continue
            parts = desc.split(".", 1)
            title = parts[1].strip() if len(parts) > 1 else desc.strip()
            task = Task(
                id=idx + 1000,
                title=title.split(':')[0].strip(),
                description=title.split(':')[1].strip() if ':' in title else "",
                priority=2,
                deadline=datetime.now(),
                dependencies=[]
            )
            generated_tasks.append(task)
            tasks[task.id] = task
            tasks_graph.add_node(task.id, **task.dict())
        return generated_tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
