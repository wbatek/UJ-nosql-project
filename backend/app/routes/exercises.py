from fastapi import APIRouter, HTTPException
from typing import List
from app.models.exercise import Exercise

router = APIRouter()

DUMMY_DB = [
    {
        "id": 1,
        "name": "Push Up",
        "description": "A basic upper body strength exercise.",
        "primary_muscle": "Chest",
        "secondary_muscle": ["Triceps", "Shoulders"]
    },
    {
        "id": 2,
        "name": "Squat",
        "description": "A fundamental lower body exercise.",
        "primary_muscle": "Quadriceps",
        "secondary_muscle": ["Hamstrings", "Glutes"]
    },
    {
        "id": 3,
        "name": "Pull Up",
        "description": "A compound movement that works multiple muscle groups.",
        "primary_muscle": "Back",
        "secondary_muscle": ["Biceps"]
    }
]

@router.get('/', response_model=List[Exercise])
async def get_exercises():
    """
    Get all exercises.
    """
    return DUMMY_DB

@router.get('/{exercise_id}', response_model=Exercise)
async def get_exercise(exercise_id: int):
    """
    Get a specific exercise by ID.
    """
    exercise = next((ex for ex in DUMMY_DB if ex["id"] == exercise_id), None)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise

@router.post('/', response_model=Exercise, status_code=201)
async def add_exercise(exercise: Exercise):
    """
    Add a new exercise.
    """
    new_exercise = exercise.dict()
    new_exercise["id"] = len(DUMMY_DB) + 1
    DUMMY_DB.append(new_exercise)
    return new_exercise
