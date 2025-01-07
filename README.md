# **F.R.I.D.A.Y.**

F.R.I.D.A.Y. (**"Female Replacement Intelligent Digital Assistant Youth"**) is a virtual assistant programmed in Python, designed to facilitate daily tasks through voice commands. This project places special emphasis on its ability to adapt to a variety of commands thanks to its flexibility in recognizing instructions. Inspired by the Iron Man movies, just like Tony Stark uses advanced artificial intelligence systems, this project aims to emulate that experience, providing a flexible assistant that adapts to the user's needs. [Versión Español](./README.es.md)

---

## **Main Features**

### 1. Voice Activation:
   - Activated by phrases such as "Friday, are you there?" or "Friday, are you awake?".

### 2. Execution of Custom Commands:
   - Performs useful actions like opening applications, taking screenshots, managing the system, and much more.

### 3. Dynamic and Natural Responses:
   - Interacts with personalized phrases and a friendly tone.

### 4. Flexibility in Command Recognition:
   - Detects keywords anywhere in a sentence, allowing for a more conversational use without the need for strict commands.

---

## **What makes F.R.I.D.A.Y. unique?**

Unlike other virtual assistants, F.R.I.D.A.Y. **does not require dividing instructions into exact words** to interpret commands. This is achieved by avoiding methods like `.split()` and prioritizing keyword searching.

## **Example of Flexibility:**

### Using `split` (Less Flexible)
When using `split()`, the command is divided into individual words, and each word is evaluated separately. This means the keyword must be present as a separate word within the command.
```python
def execute(self, command, voice):
   for key in self.command_dict.keys():
      if any(key in word for word in command.split()):  # Splits the command into words and searches for the keyword in each
         voice.speak(self.command_dict[key]())
         return
   else:
      voice.speak("I don't understand the command, sir.")
```
### Disadvantages of using `split()`:
- **Requires keywords to be separate:** If the keyword is joined with other words, like in a phrase such as "open browser please", the system won't detect it correctly.
- **Less tolerant of language variations:** The keyword must exactly match a separate word in the command.
- **Less flexibility:** The keyword cannot be at the beginning, middle, or end of the sentence unless separated by spaces.

---

## Without using `split` (More Flexible)
By not using `split()`, the system looks for the keyword throughout the entire command string. This means the system can find the keyword even if it's joined with other words or in different parts of the sentence, offering much more flexibility in how users can express the command.

```python
def execute(self, command, voice):
   for key in self.command_dict.keys():
      if key in command:  # Searches for the keyword throughout the command
         voice.speak(self.command_dict[key]())
         return
   else:
      voice.speak("I don't understand the command, sir.")
```

### Advantages of not using `split()`:
- **Greater flexibility:** The keyword can be anywhere in the command, without needing to be separated by spaces.
- **Tolerant of language variations:** Even if the command has additional words or a different structure, the system will still detect the keyword correctly.
- **Better handling of more complex or natural commands:** The system can handle longer or more complex phrases without requiring them to fit into a rigid structure.

## **Scenarios:**

### 1. Exact Command: `"browser"`
- The command is exactly "browser", which matches 100% with the keyword.
- The system identifies the match and executes the corresponding action without issues.

### 2. Conversational Phrase: `"Could you open the browsers, please?"`
- Although the phrase contains more words and is more complex, the system doesn't need the words to be separated or in a specific order.
- The system searches for the keyword "browser" throughout the sentence.
- Since the word "browser" is present, the system executes the associated action correctly.

---

## **Installation and Setup**

### Prerequisites

1. Python 3.8+
2. A functional microphone for voice recognition.
3. Libraries: `speech_recognition`, `pyttsx3`, `pyautogui`, `subprocess`, `datetime`, `time`, `random`

## **Installation**

### 1. Clone this repository:
   ```bash
   git clone https://github.com/mcortezv/F.R.I.D.A.Y. F.R.I.D.A.Y
   ```

### 2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Run the assistant:
   ```bash
   python main.py
   ```

### 4. Activate F.R.I.D.A.Y. with phrases like:
   - "Viernes estás ahí"
   - "Viernes estás despierta"

### 5. Pronounce commands like:
   - "¿Qué hora es?"
   - "Abre el navegador."
   - "Haz una captura de pantalla."

---

## **Available Commands**

| **Keyword**         | **Action**                           |
|---------------------|--------------------------------------|
| `viernes`           | Responds to your request.            |
| `hora`              | Indicates the current time.          |
| `apagar`            | Shuts down the system.               |
| `captura`           | Takes a screenshot.                  |
| `escritorio`        | Minimizes or restores windows.       |
| `teclado`           | Changes the keyboard layout.         |
| `configuracion`     | Opens system settings.               |
| `terminal`          | Opens the command terminal.          |
| `archivos`          | Opens the file explorer.             |
| `tareas`            | Opens the task manager.              |
| `navegador`         | Opens the browser.                   |
| `notas`             | Opens the notepad.                   |
| `calculadora`       | Opens the calculator.                |
| `word`              | Opens Microsoft Word.                |
| `copiar`            | Copies the current selection.        |
| `v`                 | Pastes the copied content.           |
| `z`                 | Undoes the last change.              |
| `x`                 | Cuts the current selection.          |
| `todo`              | Selects all content.                 |
| `f4`                | Closes the active window.            |
| `recarga`           | Refreshes the active page.           |

---

## **Customization**

### How to add new commands

#### 1. Open the `command.py` file.
#### 2. Add a new key and a custom function in the `command_dict` dictionary:
   ```python
   "new_command": self.my_custom_function
   ```
#### 3. Define the corresponding function:
   ```python
   def my_custom_function(self):
       # Custom logic
       return "Executing my new command."
   ```
#### 4. Save the changes and restart the assistant.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for more details.