#----------------------------------------- Ana de la Cerda ---------------------------------------
# I will use this code to check the Models programm
# is a basic test because at the first moment I didn't think about how many attribute I want to use.
# with more attribute I only need to add the to the code
#----------------------------------------------------------------------------------------------------
from apps.api.core.models import Usuario, Datos

def main():
    user_diary= USUario(name="Lucia", event=["event1", "Event2"])
    user_data= Datos(event= "Evento3")

    print(f" User history: {user_diary} | Today event: {user_data}")


if __name__ == "__main__":
    main ()