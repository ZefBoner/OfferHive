from telegram import Update
from telegram.ext import (Application,
                          CommandHandler,
                          MessageHandler,
                          filters,
                          ContextTypes)
from dotenv import load_dotenv
import os

load_dotenv()

# ESto sirve para crear comandos, este por ejemplo es "start"
async def start(update: Update,
                context: ContextTypes):
    await update.message.reply_text("Hola, soy un mensaje de prueba\
                                    estoy aqui para ayudarte")

# La siguiente funcion servira para responder mensajes con elifs

def answer(text: str):
    text = text.lower()
    if "hola" in text:
        return "Hola, como estas cachorrita?"
    elif "adios" in text:
        return "No te vayas cachorrita"

# Funcion para responder al usuario dependiendo el
# mensaje encontrado en la lista de arriba

async def chat_message(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
    type = update.message.chat.type
    if type == "private":
        text = update.message.text
        response = answer(text)
        await update.message.reply_text(response)


if __name__ == "__main__":
    app = Application.builder().token("6332076176:AAFtght4HB-").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, chat_message))
    app.run_polling(poll_interval = 1)
  

