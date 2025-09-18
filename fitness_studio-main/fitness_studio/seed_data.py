from datetime import datetime, timedelta
from app.models import FitnessClass
from app.database import fitness_classes, class_id_counter

def seed_classes():
    global class_id_counter
    now = datetime.now()

    classes = [
        {"name": "Yoga", "instructor": "Netaji", "slots": 5},
        {"name": "Zumba", "instructor": "Sai", "slots": 10},
        {"name": "HIIT", "instructor": "Akash", "slots": 8},
    ]

    for i, cls in enumerate(classes):
        fitness_classes.append(
            FitnessClass(
                id=class_id_counter,
                name=cls["name"],
                date_time=now + timedelta(days=i+1),
                instructor=cls["instructor"],
                available_slots=cls["slots"]
            )
        )
        class_id_counter += 1
