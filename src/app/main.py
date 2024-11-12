from fastapi import FastAPI
from api import router


app = FastAPI(
    title="Fast API Robinson",
    version="0.1.0",
    description="Fast API Robinson",
)

app.include_router(router)