import speech_recognition as sr
import pyttsx3


class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("voice", self.engine.getProperty("voices")[0].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language = "es").lower()
        except sr.UnknownValueError:
            return ""

    def activation(self):
        with sr.Microphone() as source:
            print("F.R.I.D.A.Y.")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio, language = "es").lower()
            return "viernes estas ahi" in text or "viernes estas despierta" in text
        except sr.UnknownValueError:
            return False