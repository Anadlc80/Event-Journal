# <---------------------------------------------- Ana de la Cerda ---------------------------------
# This file contein the functions to save and show the information about the user and its data
# We are going to divide the acctions in 4  differents functions to be more clear in the code.
# 1) crear_usuario: we create a new json file only for a user
# 2) leer_informacion:  return all the profile of the user
# 3) leer_eventos: return only the list of events for this user
# 4) anadir_informacion: is a new session of the user to save new data
# First as a faster option we are going to use a file Json for testing
# However I will use a database in the future.
#--------------------------------------------------------------------------------------------------

import json
import os   # this is going to be necessary to know if the file exists.
from typing import List
from models import Usuario, Datos   # I import the both classes that I create before for the users.



# Create the JSON file name for our user
def _user_file(name:str):
    return f"{name.lower()}.json"


#1) Create user
def crear_usuario(user: Usuario):
    path= _user_file (user.name)
    if os.path.exists(path):
        raise FileExistsError (f" The user {user.name} is alreedy in our system")
    with open(path, "w", encoding="utf-8") as fichero:
        json.dump(user.model_dump(), fichero, ensure_ascii=False, indent=4)
        #Convert the diccionary in text and safe it inside fichero. 4 is the number of spaces. Also each no Ascii character will be unicode (kept ñ, tildes)


#-------------------------------------------------------------------------------------

def leer_informacion(name:str):
    path =_user_file(name)
    # we need to check is the user is already in the system
    if os.path.exists(path):
        raise FileExistsError (f" The user {name} doesn't exist in our system")

    with open(path, "r", encoding="utf-8") as fichero:
        data= json.load(fichero)    
    
    return Usuario(**data)  # I used ** to avoid the name of the attributes and return only the value insdie of them



#------------------------------------------------------------------------------------------

def agregar_evento( name:str, nuevo:Datos):

    # The new event have to be add at the end of the list with the list function append.
    user= leer_informacion(name)
    user.list_events.append(nuevo)

    #Now we have to update the json file
    with open(_user_file(name), "W", encondig="utf-8") as fichero:
        json.dump(user.model_dump(), fichero, ensure_ascii=False, indent=4)
    
    return user


#--------------------------------------------------------------------------------------------

def leer_eventos(nave:str):
    return leer_informacion(name).list_events
