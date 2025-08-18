# Here I'm going to defin two new classes
# 1st one the class Nino which has all the attribute that we need to know about them
# 2nd the class Emociones where we can save the different emotions they will have along the time.

from pydantic import BaseModel
from typing import List
from datetime import datetime

class Nino(BaseModel):
    name:str 
    emotions: List[str] =[]


class Emociones(BaseModel):
    emotion: str
    timestamp: str= datetime.now().strftime("%Y-%M-%D  %H:%m")