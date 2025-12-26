import pyttsx3

text_to_speak = "This is an example of text to speech using pyttsx3."
text_to_speak1 = "how are you?"

# Initialize the engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

# Convert text to speech
engine.say(text_to_speak1)

# Play the speech
engine.runAndWait()