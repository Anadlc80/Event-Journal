#--------------------------------    Ana de la Cerda  -------------------------------------------------------------
# Simple file to check the different elemsemts created in storage
# I created and user, show first his empty list, then add an event, check all the information
# and also the list events again too.
#-----------------------------------------------------------------------------------------------------------------

from apps.api.core.storage import crear_usuario, leer_informacion, agregar_evento, leer_eventos
from apps.api.core.models import Datos, Usuario
from pydantic import BaseModel,Field

# This is a simple test to check the storage file, you must to change the name.
# I have to improve it, because checks that crear_usuario raises an exception if the user already exists
def main ():
    user_name= "Prueba12"
    # Create a new user with an empty list of events
    user= Usuario(name= user_name ,list_events=[])
    crear_usuario(user)
    print( "Usuario created")

    # Check the function return a message if the list is empty
    print (" The events in your list are :", leer_eventos(user_name)) 

    # Add a new event
    nuevo_evento = Datos(Event="Meeting 1", Calification=5)
    agregar_evento(user_name,nuevo_evento)
    print(" The event has beed add to your diary")

    # Show all the information of the user
    usuario= leer_informacion(user_name)
    print("The information of the user is: ", usuario)


    # We check again the list of events
    print("The list of events are:", leer_eventos(user_name))



if __name__ == "__main__":
    main()

