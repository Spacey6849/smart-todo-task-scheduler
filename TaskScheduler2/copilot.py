from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so your frontend (or testing tool) can call these APIs

# In-memory storage for tasks
tasks = []
task_id_counter = 1


def score_task(task_text):
    """
    A heuristic scoring function that simulates an AI understanding of task urgency.
    Keywords boost or reduce the score:
      • "urgent" or "asap": +20 points
      • "today": +15 points
      • "tomorrow": +10 points
      • "deadline": +10 points
      • "important": +5 points
      • "after": -5 points (implying dependency on a preceding task)
      • "before": +3 points (possibly a prerequisite)
    """
    score = 0
    text = task_text.lower()

    if "urgent" in text or "asap" in text:
        score += 20
    if "today" in text:
        score += 15
    if "tomorrow" in text:
        score += 10
    if "deadline" in text:
        score += 10
    if "important" in text:
        score += 5
    if "after" in text:
        score -= 5
    if "before" in text:
        score += 3

    return score


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Returns a JSON list of tasks sorted in descending order based on their score.
    """
    sorted_tasks = sorted(tasks, key=lambda task: task['score'], reverse=True)
    return jsonify(sorted_tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Adds a new task. Expects JSON input with a "text" field.
    Example JSON:
      { "text": "Finish the report by tomorrow because it's urgent." }
    Computes the score using `score_task` and assigns a unique id.
    """
    global task_id_counter
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing task text"}), 400

    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "Task cannot be empty"}), 400

    task_score = score_task(text)
    new_task = {
        "id": task_id_counter,
        "text": text,
        "score": task_score
    }
    tasks.append(new_task)
    task_id_counter += 1

    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Deletes a task with the given id.
    """
    global tasks
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) == len(tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks[:] = new_tasks
    return jsonify({"message": "Task deleted successfully"}), 200


@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    """
    Returns the top recommended task (highest score) as JSON.
    If there are no tasks, returns { "recommendation": None }.
    """
    if not tasks:
        return jsonify({"recommendation": None})

    # Get the task with the highest score
    recommendation_task = max(tasks, key=lambda task: task['score'])
    return jsonify({"recommendation": recommendation_task})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Smart Task Scheduler API!"})



if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) and port 5000 – this is useful for Replit & testing tools.
    app.run(host='0.0.0.0', port=5000, debug=True)
