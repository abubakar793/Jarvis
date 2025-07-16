import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import time

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Speed
engine.setProperty('volume', 1.0)  # Volume

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print(f"🧠 You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    return command

def jarvis():
    speak("Hello! I'm your assistant Jarvis. How can I help you?")

    while True:
        command = take_command()

        if 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open cmd' in command or 'open command prompt' in command:
            speak("Opening Command Prompt")
            os.system("start cmd")

        elif 'open file explorer' in command:
            speak("Opening File Explorer")
            os.system("explorer")

        elif 'show desktop' in command:
            speak("Showing desktop")
            os.system('powershell -command "(New-Object -ComObject Shell.Application).MinimizeAll()"')

        elif 'shutdown' in command:
            speak("Shutting down the system in 10 seconds. Cancel if you want.")
            os.system("shutdown /s /t 10")

        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that command.")

# Run Jarvis
jarvis()
