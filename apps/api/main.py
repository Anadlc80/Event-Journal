# Initial code for our program

# I have to import the libray fastapi to create our web server & app where I have the paths 
from fastapi import FastAPI
# from core import app as core_app 

# We create a objet of the fastApi class which have different parameters to use it later.
app= FastAPI(title= "My inner Adventure", description="Plataform for analyzing children emontions, saving these information to evaluate the resolts with AI support", version="1.0")

#Now we have to include the routes
# app.include_router(core_app.router)

@app.get("/")
def read_root():
    return " Welcome to Your Inner Adventure"
