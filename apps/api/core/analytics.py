#---------------------------------------  Ana de la Cerda ----------------------------------------------------------------------------------
# I'm going to use the python's library matplotlib to realize some operations with the events safe for each user.
# 1) Average : very usefull to know for example is a company want to know the means spent of a client
# 2) Min/Max Cualification of an event: for expample the users would know which was their best or wrost sport session ormeeting event
# 3) A graphic of the evolution the events during the time with their Cualifications
#---------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt 
from typing import List, Tuple, Optional
from apps.api.core.models import Datos


# Average of the Cualification
def media_calificacion (events: List[Datos]):
    if not events:
        return 0.0
    total=0
    for event in events:
        total+=event.Calification

    return total/len(events)


#--------------------------------------------------------------------------------------------------------------


# This function return the events with the min and max Cualifications
# Here we could use the min and max function but I wanted to do it manually.

def min_max_calificacion (events: List[Datos]):
    if not events:
        return None, None
    
    min_event= events [0]
    max_event= events [0]
    for event in events:
        if event.Calification< min_event.Calification:
            min_event= event
        if event.Calification> max_event.Calification:
            max_event= event
    
    return (min_event.Event, min_event.Calification), (max_event.Event, max_event.Calification)




#-------------------------------------------------------------------------------------------------------------------------


# Here the app shows to the user a graphic of the evolution of their events and their Cualification


def grafico_eventos ( events):
    if not events:
        return "There are not events to analyze"

    events_coord= sorted(events, key=lambda event: event.timestamp)

    x=[event.timestamp for event in events_coord]
    y=[event.Calification for event in events_coord]

    plt.figure(figsize=(8,4))
    plt.plot(x, y, marker="o", linestyle="-", color ="blue")
    plt.xticks (rotation=45, ha="right")
    plt.xlabel(" Dates ")
    plt.ylabel("Calification")
    

    plt.tight_layout()
    plt.title("Events over the time")
    plt.show()






