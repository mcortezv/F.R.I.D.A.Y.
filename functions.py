import speech_recognition, pyttsx3, pywhatkit, datetime

# Configuración del Reconocimiento de Voz
r = speech_recognition.Recognizer()


# Configuración de Voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Activar Asistente
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
    
    
# Funcion para Escuhar Instrucción 
def instruction():
    with speech_recognition.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio,language='es')
        print("Instruccion Detectada..." + texto)
        return texto.lower()
    except speech_recognition.UnknownValueError:
        return ""
    
    
# Funcion Hablar
def speak(texto):
    engine.say(texto)
    engine.runAndWait()


# Funcion para la Hora
def time():
    return datetime.datetime.now().strftime('%H:%M:%S')


# Funcion para Reproducir
def play(name):
    pywhatkit.playonyt(name)
    

    

