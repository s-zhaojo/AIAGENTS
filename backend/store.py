import json
from uuid import uuid4

DATA_FILE = 'tasks.json'

def get_all_tasks():
    try:
         with open(DATA_FILE, 'r') as file:
              return json.load(file)
    except FileNotFoundError:
         return []
    
def add_task(task):
     # unique task id
     task["id"] = str(uuid4())
     tasks = get_all_tasks()
     tasks.append(task)
     with open(DATA_FILE, 'w') as file:
          json.dump(tasks, file, indent=2)
     return task

def delete_task(task_id):
     tasks = get_all_tasks()
     tasks = [t for t in tasks if t["id"] != task_id]
     with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)
     return {"deleted": task_id}