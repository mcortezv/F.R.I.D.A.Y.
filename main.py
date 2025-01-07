from command import Command
from voice import Voice

"""
    Project - F.R.I.D.A.Y.

    @author Cortez, Manuel
    @date 06/01/2025
    
    Main Class
"""

class Assistant:
    def __init__(self):
        self.voice = Voice()
        self.command = Command()
        self.activated = False

    def run(self):
        while True:
            if not self.activated:
                if self.voice.activation():
                    self.activated = True
                    self.voice.speak(Command.random_response(["Para usted siempre, señor... ¿En qué puedo ayudarle?", 
                                                              "Así es, señor... ¿En qué puedo ayudarle?"]))
            else:
                command = self.voice.listen()
                if "dormir" in command:
                    self.voice.speak(Command.random_response(["Hasta pronto, señor. Apagada...", 
                                                              "Muy bien, señor. Fue un gusto ayudarlo. Apagada..."]))
                    break
                else:
                    self.command.execute(command, self.voice)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()