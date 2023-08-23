import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 100)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text_to_speak = input("Enter the text you want the robot to say: ")
        if text_to_speak == "q":
            speak("Bye Bye friend")
            break
        speak(text_to_speak)