from fastapi import FastAPI
from database import engine, Base
from routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Construction Task Manager API for tsting"}


app.include_router(router)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
