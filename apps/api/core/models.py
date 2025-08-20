# -----------------------------------  Ana de la Cerda -----------------------------------------------------
# Here I'm going to define two new classes
# 1st the class Datos where we can save the different events they will have along the time.
# 2nd one the class Usuario which has all the attribute that we need to know about this specific event
# One of the atributtes will be a list of the Class Datos created before
#------------------------------------------------------------------------------------------------------------


from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel,Field

class Datos (BaseModel):
    Event: str
    Calification: int
    timestamp: str= datetime.now().strftime("%Y-%m-%d  %H:%m")


class Usuario(BaseModel):
    name:str 
    age: Optional[int]= None
    sector: Optional[str]= None
    list_events: List[Datos] = Field(default_factory=list)  # We need it to create a new list for each user
