from typing import List
from app.models import FitnessClass, Booking

# Simulate in-memory DB
fitness_classes: List[FitnessClass] = []
bookings: List[Booking] = []

# Auto-increment IDs
class_id_counter = 1
booking_id_counter = 1
