import uvicorn
from fastapi import FastAPI

from database import  engine
from routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title='TaskTracker')


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
