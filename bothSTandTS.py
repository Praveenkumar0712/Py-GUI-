import pyttsx3
import speech_recognition as sr
import webbrowser as wb


def speak(text_to_speak):
    engine = pyttsx3.init()
    engine.say(text_to_speak)
    engine.runAndWait()

def voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return " Sorry, could not understand audio."
        except sr.RequestError:
            return " Could not request results from Google Speech Recognition service."

text=voice()
print(text)
if text=="hi hello":
    speak("hello, welcome to livewire")
elif "google" in text.lower():
    wb.open("https://www.google.com/search?q="+text)
else:
    speak("Welcome praveen"+text)