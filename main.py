from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

driver = ''
def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
speak("Hello master! ")

while True:
    query = recognize_speech()
    print(query)
    if query != 'Error':
        if driver != '':
         print('')
        else:
            driver = webdriver.Chrome(r'C:\Users\Kurd Tech\PycharmProjects\pythonProject\\chromedriver.exe')

        driver.maximize_window()

        if query.lower() == 'youtube':
            driver.get('https://youtube.com')
        elif query == 'exit':
                speak('Goodbye Master!')
                driver.quit()
                break
        elif query =='go back':
            driver.back()
        elif query == 'go forward':
            driver.forward()
        elif query.lower() == 'facebook':
            driver.get('https://facebook.com')
        else:
          driver.get('https://google.com')
          element = driver.find_element_by_name('q')
          element.clear()
          element.send_keys(query)
          element.send_keys(Keys.RETURN)
