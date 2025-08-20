
#---------------------------------------------- Ana de la Cerda --------------------------------------------
# Small code to test the analytics file
#----------------------------------------------------------------------------------------------------------


from apps.api.core.models import Datos
from apps.api.core.analytics import media_calificacion, grafico_eventos, min_max_calificacion


def main():
    events=[Datos(Event= "Meeting 1", Calification= 5, timestamp="2025-08-01 10:00"),
    Datos(Event= "Meeting 2", Calification= 2, timestamp="2025-08-03 10:00"),
    Datos(Event= "Meeting 3", Calification= 7, timestamp="2025-08-09 10:00")]

    avg= media_calificacion(events)
    print ("The average of the calification is ", avg)
    min_event, max_event= min_max_calificacion(events)
    print ("Minimun event", min_event)
    print ("Maximun event", max_event)


    print (" Lineal graph")
    grafico_eventos(events)



if __name__ == "__main__":
    main()



