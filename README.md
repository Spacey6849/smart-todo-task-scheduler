AI Smart Task(T-Buddy): it is an AI tool used for Scheduling your tasks and asking ai to reschedule your tasks based on the priority which will help you in doing your tasks on time and preventing the deadline

✨ AI Smart Scheduler Features
🎯 Priority-Based Rearrangement
Tasks auto-sort by priority (Low, Medium, High).

⏰ Deadline Awareness
Urgent tasks move up; countdown timers for deadlines.

🧠 Contextual Rescheduling
AI estimates task duration and handles dependencies.

🔔 Smart Notifications
Reminders for high-priority and urgent tasks.

📅 Calendar Sync
Integrates with Google Calendar, Outlook, etc.

💡 AI Suggestions
Breaks tasks into subtasks; suggests optimal times.

⚙️ Custom Rules
Set custom priorities; manually override AI.

👥 Team Collaboration
Sync team tasks; optimize shared schedules.



## 🎯 How It Works

1. **Sign Up:** Register to start using the tool.
2. **Sign In:** Log in to manage your tasks.

⚠️ **Note:** The frontend and backend currently work independently, and backend development is ongoing. Full integration is still pending.

To access the FastAPI backend, visit `http://127.0.0.1:8000/docs`.

To run the FastAPI backend with Uvicorn, use this command (if the program is nested in a file):

```bash
uvicorn foldername.openaifrfr:app --reload
```

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI, Python
- **Database:** Supabase (PostgreSQL)

## 📦 Setup & Usage

```bash
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

API documentation is available at `http://127.0.0.1:8000/docs`.

