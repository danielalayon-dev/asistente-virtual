import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import chistesESP as c
wikipedia.set_lang("es")
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 145)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="es-CO")
        command = command.lower()
        if 'alexa' in command:
            command = command.lstrip('alexa ')
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'reproduce' in command:
        command = command.replace('reproduce','')
        respuesta = "Reproduciendo" + command
        talk(respuesta)
        pywhatkit.playonyt(command)
    elif 'hora' in command:
        hora_actual = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las:"+hora_actual)
    elif 'quién es' in command:
        person= command.replace('quien es','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'chiste' in command:
        chiste = c.get_random_chiste()
        talk(chiste)
    else:
        talk('Puedes decir otro comando o repitelo nuevamente')

run_alexa()