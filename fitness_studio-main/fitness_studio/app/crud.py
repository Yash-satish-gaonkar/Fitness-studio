from datetime import datetime
from typing import List
from app.models import FitnessClass, Booking
from app.schemas import BookingRequest
from app.database import fitness_classes, bookings, booking_id_counter

def list_classes() -> List[FitnessClass]:
    now = datetime.now()
    return [cls for cls in fitness_classes if cls.date_time > now]

def book_class(data: BookingRequest) -> Booking:
    global booking_id_counter

    selected_class = next((cls for cls in fitness_classes if cls.id == data.class_id), None)
    if not selected_class:
        raise ValueError("Class not found")

    if selected_class.available_slots <= 0:
        raise ValueError("No slots available")

    # Decrement slot
    selected_class.available_slots -= 1

    # Create booking
    booking = Booking(
        id=booking_id_counter,
        class_id=data.class_id,
        client_name=data.client_name,
        client_email=data.client_email,
        booked_at=datetime.now()
    )
    bookings.append(booking)
    booking_id_counter += 1
    return booking

def get_bookings_by_email(email: str) -> List[Booking]:
    return [b for b in bookings if b.client_email == email]
