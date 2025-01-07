import subprocess
import pyautogui
import datetime
import time
from random import choice
# import pywhatkit

"""
    Project - F.R.I.D.A.Y.

    @author Cortez, Manuel
    @date 06/01/2025
    
    Clase de ejecucion y creacion de nuevos comandos.
"""

class Command:
    def __init__(self):
        self.command_dict = {
            "viernes": self.reply,
            # "reproduce": self.play,
            "hora": self.hour,
            "apagar": self.shutdown,
            "captura": self.screenshot,
            "escritorio": self.desktop,
            "teclado": self.keyboard,
            "configuracion": self.config,
            "terminal": self.terminal,
            "archivos": self.files,
            "tareas": self.task,
            "navegador": self.browser,
            "notas": self.notepad,
            "calculadora": self.calc,
            "word": self.word,
            "copiar": self.ctrl_c,
            "v": self.ctrl_v,
            "z": self.ctrl_z,
            "x": self.ctrl_x,
            "todo": self.ctrl_a,
            "f4": self.alt_f4,
            "recarga": self.f5
        }
    
    def  execute(self, command, voice):
        for key in self.command_dict.keys():
            if key in command:
                voice.speak(self.command_dict[key]())
                return
        else:
            voice.speak("No comprendo la instrucción señor.")
        
    @staticmethod
    def random_response(responses):
        return choice(responses)

    def reply(self):
        return Command.random_response(["¿Si, señor?", "Dígame, señor.", "¿En qué puedo servirle, señor?", "Siempre a sus órdenes, señor."])
    
    # def play(self, command):
    #     pywhatkit.playonyt(command.replace("reproduce", "").strip())
    #     return "Ahora mismo, señor."
        
    def hour(self):
        return "La hora actual es: " + datetime.datetime.now().strftime("%H:%M:%S")
        
    def shutdown(self):
        self.terminal() 
        time.sleep(1.5)
        pyautogui.write("shutdown /s /t 0")
        pyautogui.press("enter")
        return ""
    
    def screenshot(self):
        pyautogui.hotkey("alt", "f1")
        return "Capturando"
        
    def desktop(self):
        pyautogui.hotkey("win", "d")  
        return "Listo"
        
    def keyboard(self):
        pyautogui.hotkey("win", "space")
        return "Cambio de ditribucion confirmado"
        
    def config(self):
        pyautogui.hotkey("win", "i")
        return "Con gusto"
        
    def terminal(self):
        pyautogui.hotkey("win", "r")  
        pyautogui.write("wt")
        pyautogui.press("enter")
        return "Bienvenido señor"
        
    def files(self):
        pyautogui.hotkey("win", "e")
        return "Abriendo explorador"
        
    def task(self):
        pyautogui.hotkey("ctrl", "shift", "esc")
        return "Abriendo administrador de tareas"
        
    def browser(self):
        pyautogui.hotkey("win", "r")  
        pyautogui.write("chrome")
        pyautogui.press("enter")
        return "Abriendo navegador."
        
    def notepad(self):
        subprocess.Popen(["notepad.exe"])
        return "Abriendo el Bloc de notas."
        
    def calc(self):
        subprocess.Popen(["calc.exe"])
        return "Abriendo la calculadora."
        
    def word(self):
        pyautogui.hotkey("win", "r")  
        pyautogui.write("winword")
        pyautogui.press("enter")
        return "Ahora mismo he abierto un word para usted"
        
    def ctrl_c(self):
        pyautogui.hotkey("ctrl", "c")  
        return "Copiando seleccion"
        
    def ctrl_v(self):
        pyautogui.hotkey("ctrl", "v")
        return "Pegando texto."
        
    def ctrl_z(self):
        pyautogui.hotkey("ctrl", "z")
        return "Deshaciendo último cambio."
        
    def ctrl_x(self):
        pyautogui.hotkey("ctrl", "x")
        return "Cortando seleccion"
        
    def ctrl_a(self):
        pyautogui.hotkey("ctrl", "a") 
        return "He seleccionado todo"
        
    def alt_f4(self):
        pyautogui.hotkey("alt", "f4")
        return "Ventana cerrada."
        
    def f5(self):
        pyautogui.press("f5") 
        return "Actualizando pagina"