from fastapi import APIRouter, routing
from .schema import EventListSchema, EventSchema

from fastapi import FastAPI

router = APIRouter()

#GEt /api/events/
@router.get("/")
def read_events() -> EventListSchema: 
    return {
        "results": [
            {"id":1},{"id":2},{"id":3}
            ],
            "count": 3
    }

#GEt /api/events/
@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchema: 
    return {"id":event_id}


#Send Data Here
# Create View

@router.post("/")
def create_event(data:dict={}) -> EventSchema: 
    return {"id":123}