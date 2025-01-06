import speech_recognition, pyttsx3, pywhatkit, datetime

r = speech_recognition.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)

def activation():
    with speech_recognition.Microphone() as source:
        print("F.R.I.D.A.Y.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='es')
        if 'viernes estas ahi?' or 'viernes estas despierta?' in text:
            return True
    except speech_recognition.UnknownValueError:
        return False
     
def listen():
    with speech_recognition.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es")
        print("Instruccion Detectada..." + texto)
        return texto.lower()
    except speech_recognition.UnknownValueError:
        return ""

def speak(texto):
    engine.say(texto)
    engine.runAndWait()

def time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def play(name):
    pywhatkit.playonyt(name)