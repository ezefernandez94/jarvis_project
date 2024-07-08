import speech_recognition as sr

## Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    ## Use default mic by default
    ## TODO: check for more options (earbuds, etc.)
    with sr.Microphone() as source:
        print("Listening ..")

        ## Adjustment for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        ## Listen to user's input
        audio_data = recognizer.listen(source)
    
        try:
            print("Recognizing ..")

            ## Recognize data using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)

            print(f"Speech recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None
        
## Call the function for listening
recognized_text = listen()