from datetime import datetime
from typing import List
from pydantic import BaseModel

class FitnessClass(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: str
    booked_at: datetime
