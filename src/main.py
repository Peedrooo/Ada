from fastapi import FastAPI
from app.routers.setup import classrom, discipline, teacher

import uvicorn

app = FastAPI()

app.include_router(classrom.router)
app.include_router(discipline.router)
app.include_router(teacher.router)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "APP IS RUNNING - Welcome to the ADA API"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
