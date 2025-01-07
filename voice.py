import speech_recognition as sr
import pyttsx3

"""
    Project - F.R.I.D.A.Y.

    @author Cortez, Manuel
    @date 06/01/2025
    
    Clase encargada del reconocimiento de voz y activacion del asistente.
"""

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("voice", self.engine.getProperty("voices")[0].id)
        
    def activation(self):
        with sr.Microphone() as source:
            print("F.R.I.D.A.Y.")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio, language = "es").lower()
            return "viernes" in text or "despierta" in text
        except sr.UnknownValueError:
            return False

    def listen(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language = "es").lower()
        except sr.UnknownValueError:
            return ""
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()