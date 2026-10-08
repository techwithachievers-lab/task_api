from fastapi import FastAPI

app = FastAPI(title="Task Manager API")


tasks = [  
    {
        "ID": 1,
        "Title": "Learn Ai Engineering",
        "Completed": True
    },
    {
         "ID": 2,
         "Title": "Learn Ai Automation",
         "Completed": True
    }  
    
    ]


@app.get("/")
def home():
    return{
        "Message": "Task Manager Api in progress"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/api")
def get_api():
    return {
        "Message": "Hi, Nothing to see here, check the tasks route"
    }
