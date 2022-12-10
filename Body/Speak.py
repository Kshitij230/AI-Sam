"""
Two Speak functions are there
1 - Windows Based
2 - Browser Based
"""

"""
--- Windows Based ---
Advantages:
    a) Fast
    b) Offline
Disadvantages:
    a) Can't Overspeak
    b) Less Voices

"""

# import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[0].id)
#     engine.setProperty('rate', 170)
#     print()
#     print(f"You: {Text}.")
#     print()
#     engine.say(Text)
#     engine.runAndWait()

# To save the voice of the assistant as audio file --- engine.save_to_file("Name of the audio file")


## --------------------------------------------------------------------------------------------------- ##

"""
Chrome Based

Advantages:
    a) More voices
    b) More clear
    c) Can Overspeak
Disadvantages:
    a) Slow

"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
# log-level:
# Sets the minimum log level.
# Valid values are from 0 to 3: 
#     INFO = 0, 
#     WARNING = 1, 
#     LOG_ERROR = 2, 
#     LOG_FATAL = 3.
# default is 0.
chrome_options.headless = True
Path = "E:\Sam-Env\AI-Sam\DataBase\chromedriver.exe"
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

# website = "https://readloud.net/"
website = "https://ttsreader.com/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div/div[1]/div[5]/select[1]"))
ButtonSelection.select_by_visible_text("English, US, Microsoft Mark - English (United States)")
ButtonSelection = Select(driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[3]/div/div[1]/div[5]/select[2]"))
ButtonSelection.select_by_visible_text("Slow")
print("\nReady to go...")

def Speak(Text):
    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass
    else:
        print()
        print(f"Sam: {Text}")
        print()
        Data = str(Text)
        xpathofsec = '/html/body/div[1]/div[2]/div[3]/div/div[1]/div[7]/textarea[1]'
        driver.find_element(by=By.XPATH, value=xpathofsec).clear()
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH, value='//*[@id="play_button"]').click()
        driver.find_element(by=By.XPATH, value=xpathofsec).clear()

        if lengthoftext>=30:
            sleep(4)
        elif lengthoftext>=40:
            sleep(6)
        elif lengthoftext>=55:
            sleep(8)
        elif lengthoftext>=70:
            sleep(0)
        elif lengthoftext>=100:
            sleep(13)
        elif lengthoftext>=120:
            sleep(14)
        else:
            sleep(2)
