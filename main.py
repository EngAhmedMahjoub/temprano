import os
from dotenv import load_dotenv
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_USERNAME: final = '@ttemprano_bot'

# Set your token using .env file
load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE)
    await update.message.reply_text('Hello, I am your friendly assistant temprano! How can I help you?')
    