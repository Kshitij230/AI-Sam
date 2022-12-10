# Command in Hindi or English
# Excecution in only English

# Step: 1
# pip install googletrans==3.1.0a0

# Step: 2
# Three functions
# 1 - Listening Function
# 2 - Translation to English
# 3 - Connection

import speech_recognition as sr
from googletrans import Translator

# 1 - Listening in Hindi or English Both

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8) # Listening Mode...

    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio,language='hi')

    except:
        return ""

    query = str(query).lower()
    if len(query)>1:
        return query
    else:
        return None


# 2 - Tranlating Hindi to English

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line, 'en')
    data  = result.text
    if len(data)<1:
        pass
    else:
        print(f"You: {data}")
    return data

# 3 - Connecting Above functions

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data
