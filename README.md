# AI Smart Task (T-Buddy)

**AI Smart Task (T-Buddy)** is an AI-powered tool designed to help you schedule tasks efficiently and reschedule them based on priority. It ensures timely task completion while preventing missed deadlines.

---

## ✨ AI Smart Scheduler Features

✅ **Priority-Based Rearrangement** – Tasks auto-sort by priority (Low, Medium, High).  
✅ **Deadline Awareness** – Urgent tasks move up with countdown timers for deadlines.  
✅ **Contextual Rescheduling** – AI estimates task duration and handles dependencies.  
✅ **Smart Notifications** – Get reminders for high-priority and urgent tasks.  
✅ **Calendar Sync** – Integrates with Google Calendar, Outlook, and more.  
✅ **AI Suggestions** – Breaks tasks into subtasks and suggests optimal times.  
✅ **Custom Rules** – Set custom priorities with manual overrides.  
✅ **Team Collaboration** – Sync and optimize shared team tasks.  

---

## 🎯 How It Works

1. **Sign Up** – Register to start using the tool.  
2. **Sign In** – Log in to manage your tasks.  

⚠️ **Note:** The frontend and backend currently work independently. Backend development is ongoing, and full integration is in progress.

🔗 **To access the FastAPI backend**, visit: `http://127.0.0.1:8000/docs`

📌 **Run the FastAPI backend with Uvicorn:**
```sh
uvicorn foldername.openaifrfr:app --reload
```

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** FastAPI, Python  
- **Database:** Supabase (PostgreSQL)  

---

## 📦 Setup & Usage

```sh
# Clone the repository
git clone https://github.com/Spacey6849/smart-todo-task-scheduler.git

# Navigate to the project directory
cd smart-todo-task-scheduler

# Set up and activate the virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI backend
uvicorn openaifrfr:app --reload
```

📌 API documentation is available at `http://127.0.0.1:8000/docs`.

---

## 🚀 Current Development Status

Currently, the frontend and backend are working **independently**. The integration process is **in progress** to enable seamless communication between both components.

Stay tuned for updates! 🚀

📸 Screenshots

**Homepage**
![Homepage](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/85ba7f58525736c402558ab847542687af2f57ed/Images/homepage.jpg)


**Task Creation**

![TaskCreation](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/85ba7f58525736c402558ab847542687af2f57ed/Images/homepage.jpg)

__________________________________________________________________________________________________________________________________________________________

![TaskCreation](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/CreateTask.jpg)

**User Authentication**
![UserAuthentication](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/signIn1.jpg)

![UserAuthentication](https://github.com/Spacey6849/smart-todo-task-scheduler/blob/dc710bc532b1ebb792a045ddfa8f1f4d6f711496/Images/signup1.jpg)
