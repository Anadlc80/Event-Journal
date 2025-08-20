#------------------------------- Ana de la Cerda -------------------------------------------------------------------------------------
# Initial code for our program, this is going to be the start of the app
# This is just a prototype  with a code that could be use in very different enviroments
# It could be a diary of reunios, dates, sport trainning....
# Even the app for a small companies where the can keep the details of the clients and reunion ( hair salon, estetic salon ...)
# I should only change the kind and number of atributtes of the class
#---------------------------------------------------------------------------------------------------------------------------------------

# I have to import the libray fastapi to create our web server & app where I have the paths 
from fastapi import FastAPI
# from core import app as core_app 

# I create a objet of the fastApi class which have different parameters to use it later.
app= FastAPI(title= "My Logbook", description="Plataform for record and analyze daily activities", version="1.0")

#Now we have to include the routes
# app.include_router(core_app.router)

@app.get("/")
def read_root():
    return " Welcome to Your Personal LogBook"
