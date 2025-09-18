from datetime import datetime
from pydantic import BaseModel, EmailStr

class FitnessClassOut(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    booked_at: datetime
