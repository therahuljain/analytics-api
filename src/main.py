from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.db.session import init_db


from api.events import router as events_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app start up
    init_db()
    yield
    #clean up

app = FastAPI()
app.include_router(events_router, prefix="/api/events")


@app.get("/")
def read_root():
    return {"Hello": "World2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}

