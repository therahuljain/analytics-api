import os
from fastapi import APIRouter, routing
from .schema import EventCreateSchema, EventListSchema, EventSchema, EventUpdateSchema

from fastapi import FastAPI

from api.db.config import DATABASE_URL

router = APIRouter()

#GEt /api/events/
@router.get("/")
def read_events() -> EventListSchema:
    print(DATABASE_URL)
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

# @router.post("/")
# def create_event(payload:EventCreateSchema) -> EventSchema: 
#     print(payload)
#     return {"id":123}

#Update the data
@router.post("/")
def create_event(event_id: int, payload:EventCreateSchema) -> EventSchema: 
    print(payload.page)
    data = payload.model_dump()   #payload -> dict -> pydantic
    return {"id":123, **data}

#Update this data
# PUT /api/events/12

@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventSchema: 
    print(payload.description)
    data = payload.model_dump()
    return {"id":event_id,  **data}