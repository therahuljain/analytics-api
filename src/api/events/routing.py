import os
from pydoc import importfile
from fastapi import APIRouter, Depends, routing
from .models import EventCreateSchema, EventListSchema, EventModel, EventUpdateSchema
from api.db.session import get_session
from sqlmodel import Session

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
def get_event(event_id:int) -> EventModel: 
    return {"id":event_id}


#Send Data Here
# Create View

# @router.post("/")
# def create_event(payload:EventCreateSchema) -> EventSchema: 
#     print(payload)
#     return {"id":123}

#Update the data
@router.post("/", response_model= EventModel)
def create_event( 
                    payload:EventCreateSchema, 
                    session: Session = Depends(get_session)): 
    data = payload.model_dump()   #payload -> dict -> pydantic
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

#Update this data
# PUT /api/events/12

@router.put("/{event_id}")
def update_event(event_id:int, payload: EventUpdateSchema) -> EventModel: 
    print(payload.description)
    data = payload.model_dump()
    return {"id":event_id,  **data}