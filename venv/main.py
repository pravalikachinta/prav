from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "application": "Student Management System",
        "status": "API Running Successfully"
    }