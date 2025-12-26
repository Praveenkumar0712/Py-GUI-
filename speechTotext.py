import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    try:
        audio = recognizer.listen(source, timeout=5)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
