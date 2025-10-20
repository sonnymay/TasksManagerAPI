from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import tasks

# Initialize database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Task Manager API")

# --- Enable CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # (you can restrict to frontend domain later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register router
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager API! Use /docs to explore endpoints."}
