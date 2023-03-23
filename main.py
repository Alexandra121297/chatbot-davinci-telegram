# Importar librerías
import openai
import telebot
from os import environ as env
from dotenv import load_dotenv

# Cargar env
load_dotenv()

# Inicializar los tokens y las claves de la API
openai.api_key = env["OPENAI_API_KEY"]
bot = telebot.TeleBot(env["BOT_API_KEY"])

# Definir la plantilla de la conversación creando un objeto que contenta la base de conocimiento personalizada
chatbot_prompt = """
"""

# Función de entrada y salida de mensajes
@bot.message_handler(func=lambda message: True) #decorador de telegram
def get_codex(message):

    # Definir que las respuestas tome en cuenta nuestra información personalizada
    knowledge = chatbot_prompt + f"Usuario: {message.text}\n"

    # Completar la respuesta con el modelo de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=knowledge,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)

    bot.send_message(message.chat.id,
    f'```python\n{response["choices"][0]["text"]}\n```',
    parse_mode="Markdown")
