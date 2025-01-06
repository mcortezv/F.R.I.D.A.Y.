from command import Command
from voice import Voice


class Assistant:
    def __init__(self):
        self.voice = Voice()
        self.activated = False

    def run(self):
        while True:
            if not self.activated:
                if self.voice.activation():
                    self.activated = True
                    self.voice.speak(Command.random_response(["Para usted siempre, señor... ¿En qué puedo ayudarle?", "Así es, señor... ¿En qué puedo ayudarle?"]))
            else:
                command = self.voice.listen()
                if command:
                    self.activated = Command.execute(command, self.voice)

if __name__ == "__main__":
    assistant = Assistant()
    assistant.run()