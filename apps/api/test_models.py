# I will use this code to check the Models programm

from apps.api.core.models import Nino, Emociones

def main():
    ChildDiary= Nino(name="Lucia", emotions=["Triste", "Cansado"])
    ChildEmotion= Emociones(emotion= "feliz")

    print(f" Child history: {ChildDiary} | Today emotions: {ChildEmotion}")


if __name__== "__main__":
    main()