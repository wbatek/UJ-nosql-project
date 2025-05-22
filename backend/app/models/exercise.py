from pydantic import BaseModel
from typing import List

class Exercise(BaseModel):
    id: int
    name: str
    description: str
    primary_muscle: str
    secondary_muscle: List[str]
