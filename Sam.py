from Brain.AiBrain import ReplyBrain
from Brain.QnA import QuestionAnswer
from Body.Listen import MicExecution
print("\n>> Starting Sam in few seconds ... ...\n")
from Body.Speak import Speak
from Feaures.Clap import Tester
print("\n>> Clap to start ... ...\n")

def MainExecution():

    Speak("Hello Sir")
    Speak("I'm Sam, I'm ready to assist you Sir.")

    while True:
        Data = MicExecution()
        Data = str(Data)

        if len(Data)<=2:
            pass
        
        elif "what" in Data or "who" in Data or "why" in Data or "how" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionAnswer(Data)
            Speak(Reply)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print()
        print(">> Clap Detected :) >>")
        print()
        MainExecution()
    else:
        pass

ClapDetect()
