# I will use this code to check the Models programm
# is a basic test because at the first moment I didn't think about how many attribute I want to use

from apps.api.core.models import Nino, Emociones

def main():
    ChildDiary= Nino(name="Lucia", emotions=["Triste", "Cansado"])
    ChildEmotion= Emociones(emotion= "feliz")

    print(f" Child history: {ChildDiary} | Today emotions: {ChildEmotion}")


if __name__== "__main__":
    main()