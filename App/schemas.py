from pydantic import BaseModel
from typing import List, Dict



#Learn what schemas are(Done!)

class TranslationRequest(BaseModel):
    text: str
    languages: List[str]

class TaskResponse(BaseModel):
    task_id: int

class TranslationStatus(BaseModel):
    task_id: int
    status: str
    translations: Dict[str,str]