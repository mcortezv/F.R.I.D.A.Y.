import functions as fn, sentences as st

import os
import subprocess
import pyautogui

def main():
    activated = False
    while True:
        if not activated:
            if fn.activation():
                activated = True
                fn.speak(st.wakeup())
        else:
            instruction = fn.instruction()
            if instruction == "":
                print("No se ha detectado alguna instrucción...")
            elif 'dormir' in instruction:
                fn.speak(st.sleep())
                break
            elif 'viernes' in instruction:
                fn.speak(st.reply())
            elif 'reproduce' in instruction:
                name = instruction.replace('reproduce', '')
                fn.speak("Ahora mismo señor")
                fn.play(name)
            elif 'dime la hora' in instruction:
                time_now = fn.time()
                fn.speak("La hora actual es: " + time_now)
            elif "navegador" in instruction:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                fn.speak("Abriendo navegador.")
            elif "notas" in instruction:
                subprocess.Popen(["notepad.exe"])
                fn.speak("Abriendo el Bloc de notas.")
            elif "calculadora" in instruction:
                subprocess.Popen(["calc.exe"])
                fn.speak("Abriendo la calculadora.")
            elif "nuevo" in instruction:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
                fn.speak("Ahora mismo abro word para usted.")
            elif "ventana" in instruction:
                pyautogui.hotkey('alt', 'f4')
                fn.speak("Listo")
            elif "texto" in instruction:
                pyautogui.hotkey('ctrl', 'x')
                fn.speak("Cortando")
            elif "v" in instruction:
                pyautogui.hotkey('ctrl', 'v')
                fn.speak("Ahora mismo")
            elif "z" in instruction:
                pyautogui.hotkey('ctrl', 'z')
                fn.speak("Listo")
            else:
                fn.speak("Me temo que no comprendo lo que solicito señor.")
    return
    
if __name__ == '__main__':
    main()
    