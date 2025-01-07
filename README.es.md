# **F.R.I.D.A.Y.**

F.R.I.D.A.Y. (**"Female Replacement Intelligent Digital Assistant Youth"**) es un asistente virtual programado en Python, diseñado para facilitar tareas cotidianas mediante comandos de voz. Este proyecto pone un énfasis especial en su capacidad para adaptarse a una variedad de comandos gracias a su flexibilidad en el reconocimiento de instrucciones. Inspirado en las películas de Iron Man, al igual que Tony Stark utiliza sistemas avanzados de inteligencia artificial, este proyecto busca emular esa experiencia, brindando un asistente flexible y adaptable a las necesidades del usuario.

---

## **Características Principales**

### 1. Activación por voz:
   - Se activa mediante frases como "viernes estás ahí" o "viernes estás despierta".

### 2. Ejecución de comandos personalizados:
   - Realiza acciones útiles como abrir aplicaciones, capturar pantallas, gestionar el sistema, y mucho más.

### 3. Respuestas dinámicas y naturales:
   - Interactúa con frases personalizadas y un tono amigable.

### 4. Flexibilidad en el reconocimiento de comandos:
   - Detecta palabras clave en cualquier parte de una frase, lo que permite un uso más conversacional sin la necesidad de comandos estrictos.

---

## **¿Qué hace a F.R.I.D.A.Y. único?**

A diferencia de otros asistentes virtuales, F.R.I.D.A.Y. **no requiere dividir las instrucciones en palabras exactas** para interpretar los comandos. Esto se logra evitando el uso de métodos como `.split()` y priorizando la búsqueda de palabras clave.

## **Ejemplo de flexibilidad:**

### Usando `split` (Menos flexible)
Cuando utilizas `split()`, el comando se divide en palabras individuales, y cada palabra es evaluada por separado. Esto significa que la palabra clave debe estar presente como una palabra separada dentro del comando.
```python
def execute(self, command, voice):
   for key in self.command_dict.keys():
      if any(key in word for word in command.split()):  # Divide el comando en palabras y busca la clave en cada una
         voice.speak(self.command_dict[key]())
         return
   else:
         voice.speak("No comprendo la instrucción, señor.")
```
### Desventajas de usar `split()`:
- **Requiere que las palabras clave estén separadas:** Si la palabra clave está unida a otras palabras, como en una frase como "abrir navegador por favor", el sistema no la detectará correctamente.
- **Menos tolerante a variaciones en el lenguaje:** La palabra clave debe coincidir exactamente con una palabra separada en el comando.
- **Menor flexibilidad:** No se permite que las palabras clave estén al principio, en medio o al final de la frase sin que estén separadas por espacios.

---

## Sin usar `split` (Más flexible)
Al no usar `split()`, el sistema busca la palabra clave dentro de toda la cadena del comando. Esto significa que el sistema puede encontrar la palabra clave incluso si está unida a otras palabras o en diferentes partes de la frase, lo que da mucha más flexibilidad en cómo los usuarios pueden expresar el comando.

```python
def  execute(self, command, voice):
   for key in self.command_dict.keys():
      if key in command: # Busca la palabra clave en todo el comando
         voice.speak(self.command_dict[key]())
         return
   else:
      voice.speak("No comprendo la instrucción señor.")
```

### Ventajas de no usar `split()`:
- **Mayor flexibilidad:** La palabra clave puede estar en cualquier parte del comando, sin necesidad de que esté separada por espacios.
- **Tolerante a variaciones en el lenguaje:** Incluso si el comando tiene otras palabras adicionales o una estructura diferente, el sistema seguirá detectando la palabra clave correctamente.
- **Mejor manejo de comandos más complejos o naturales:** El sistema puede manejar frases más largas o complejas sin requerir que se ajusten a una estructura rígida.

## **Escenarios:**

### 1. Comando Exacto: `"navegador"`
- El comando es exactamente "navegador", que coincide al 100% con la palabra clave.
- El sistema identifica la coincidencia y ejecuta la acción correspondiente sin problemas.

### 2. Frase Conversacional: `"¿Podrías abrir los navegadores, por favor?"`
- Aunque la frase contiene más palabras y es más compleja, el sistema no necesita que las palabras estén separadas o en un orden específico.
- El sistema busca la palabra clave "navegador" dentro de toda la frase.
- Dado que la palabra "navegador" está presente, el sistema ejecuta la acción asociada correctamente.

---

## **Instalación y Configuración**

### Requisitos Previos

1. Python 3.8+
2. Un micrófono funcional para el reconocimiento de voz.
3. Librerias: `speech_recognition`, `pyttsx3`, `pyautogui`, `subprocess`, `datetime`, `time`, `random`

## **Instalación**

### 1. Clona este repositorio:
   ```bash
   git clone https://github.com/mcortezv/F.R.I.D.A.Y.
   ```

### 2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Ejecuta el asistente:
   ```bash
   python main.py
   ```

### 4. Activa F.R.I.D.A.Y. con frases como:
   - "Viernes estás ahí"
   - "Viernes estás despierta"

### 5. Pronuncia comandos como:
   - "¿Qué hora es?"
   - "Abre el navegador."
   - "Haz una captura de pantalla."

---

## **Comandos Disponibles**

| **Palabra Clave**   | **Acción**                           |
|---------------------|--------------------------------------|
| `viernes`           | Responde a tu solicitud.             |
| `hora`              | Indica la hora actual.               |
| `apagar`            | Apaga el sistema.                    |
| `captura`           | Realiza una captura de pantalla.     |
| `escritorio`        | Minimiza o restaura ventanas.        |
| `teclado`           | Cambia la distribución del teclado.  |
| `configuracion`     | Abre la configuración del sistema.   |
| `terminal`          | Abre la terminal de comandos.        |
| `archivos`          | Abre el explorador de archivos.      |
| `tareas`            | Abre el administrador de tareas.     |
| `navegador`         | Abre el navegador.                   |
| `notas`             | Abre el bloc de notas.               |
| `calculadora`       | Abre la calculadora.                 |
| `word`              | Abre Microsoft Word.                 |
| `copiar`            | Copia la selección actual.           |
| `v`                 | Pega el contenido copiado.           |
| `z`                 | Deshace el último cambio.            |
| `x`                 | Corta la selección actual.           |
| `todo`              | Selecciona todo el contenido.        |
| `f4`                | Cierra la ventana activa.            |
| `recarga`           | Refresca la página activa.           |

---

## **Personalización**

### Cómo agregar nuevos comandos

#### 1. Abre el archivo `command.py`.
#### 2. Agrega una nueva clave y una función personalizada en el diccionario `command_dict`:
   ```python
   "nuevo_comando": self.mi_funcion_personalizada
   ```
#### 3. Define la función correspondiente:
   ```python
   def mi_funcion_personalizada(self):
       # Lógica personalizada
       return "Ejecutando mi nuevo comando."
   ```
#### 4. Guarda los cambios y reinicia el asistente.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for more details.