from fastapi import FastAPI
from backend.routes.analyze import router

app = FastAPI(title="AI Secure Data Intelligence Platform")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}
