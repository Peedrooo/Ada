from fastapi import FastAPI
from src.app.routers import setup

import uvicorn

app = FastAPI()

app.include_router(setup.router)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "APP IS RUNNING - Welcome to the ADA API"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
