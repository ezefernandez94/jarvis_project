import pyttsx3
## For more options: https://pyttsx3.readthedocs.io/en/latest/engine.html#using-pyttsx3

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

engine.setProperty('rate', 200)
engine.setProperty('voice', voices[0].id)

def speak(*args, **kwargs):

    input_speech = ""
    
    for phrase in args:
        input_speech += str(phrase)

    print(input_speech)
    
    engine.say(input_speech)
    engine.runAndWait()

speak('TU VIEJA EN TANGA', 'Y AGUANTE BOKEEEEEE')