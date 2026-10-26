
from fastapi import FastAPI

app = FastAPI(title="Multimodal Attendance Agent")

@app.get("/")
def home():
    return {
        "message": "Multimodal Attendance Agent backend is running!"
    }
