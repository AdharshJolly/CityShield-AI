from fastapi import FastAPI

app = FastAPI()

@app.post("/events")
def receive_event(event: dict):
    return {"status": "received"}
