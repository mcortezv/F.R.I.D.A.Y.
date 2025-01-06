import functions, sentences, os, subprocess, pyautogui

def main():
    activated = False
    while True:
        if not activated:
            if functions.activation():
                activated = True
                functions.speak(sentences.wakeup())
        else:
            command = functions.listen()
            if command == "viernes":
                functions.speak(sentences.reply())
            elif "dormir" in command:
                functions.speak(sentences.sleep())
                break
            elif "reproduce" in command:
                name = command.replace("reproduce", "")
                functions.speak("Ahora mismo señor")
                functions.play(name)
            elif "dime la hora" in command:
                functions.speak("La hora actual es: " + functions.time())
            elif "navegador" in command:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                functions.speak("Abriendo navegador.")
            elif "notas" in command:
                subprocess.Popen(["notepad.exe"])
                functions.speak("Abriendo el Bloc de notas.")
            elif "calculadora" in command:
                subprocess.Popen(["calc.exe"])
                functions.speak("Abriendo la calculadora.")
            elif "nuevo" in command:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
                functions.speak("Ahora mismo abro word para usted.")
            elif "ventana" in command:
                pyautogui.hotkey("alt", "f4")
                functions.speak("Listo")
            elif "texto" in command:
                pyautogui.hotkey("ctrl", "x")
                functions.speak("Cortando")
            elif "v" in command:
                pyautogui.hotkey("ctrl", "v")
                functions.speak("Ahora mismo")
            elif "z" in command:
                pyautogui.hotkey("ctrl", "z")
                functions.speak("Listo")
            else:
                functions.speak("Me temo que no comprendo lo que solicito señor.")
    
if __name__ == "__main__":
    main()