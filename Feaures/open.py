import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
    elif "open" in Query:
        Nameoftheapp = Query.replace("open ", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    elif "start" in Query:
        Nameoftheapp = Query.replace("open ", "")
        if "whatsapp" in Nameoftheapp:
            webbrowser.open("https://web.whatsapp.com")
        # pyautogui.press('win')
        # sleep(1)
        # keyboard.write(Nameoftheapp)
        # sleep(1)
        # keyboard.press('enter')
        # sleep(0.5)
        # return True

OpenExe("start whatsapp")
