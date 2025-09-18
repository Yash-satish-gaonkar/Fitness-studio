from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.schemas import FitnessClassOut, BookingRequest, BookingOut
from app.crud import list_classes, book_class, get_bookings_by_email
from app.database import fitness_classes
from seed_data import seed_classes

app = FastAPI(title="Fitness Studio")

# Seed initial data
seed_classes()

@app.get("/classes", response_model=List[FitnessClassOut])
def get_classes():
    return list_classes()

@app.post("/book", response_model=BookingOut)
def book(request: BookingRequest):
    try:
        return book_class(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/bookings", response_model=List[BookingOut])
def get_bookings(email: str = Query(..., description="Client email")):
    return get_bookings_by_email(email)
