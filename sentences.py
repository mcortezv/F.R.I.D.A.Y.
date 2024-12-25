from random import randint

# Frases Despertar
def wakeup():
    wakeup = ["Para usted siempre señor... ¿En qué puedo ayudarle?", "Así es señor... ¿En qué puedo ayudarle?"]
    i = randint(0,len(wakeup))
    return wakeup[i - 1]


# Frases Apagar
def sleep():
    sleep = ["Hasta pronto señor,   Apagada...", "Muy bien señor, fue un gusto ayudarlo,   Apagada..."]
    i = randint(0,len(sleep))
    return sleep[i - 1]


# Viernes Responde
def reply():
    reply = ["¿Si? señor", "Digame señor", "En que puedo servirle? señor", "Para usted señor? Siempre"]
    i = randint(0,len(reply))
    return reply[i - 1]