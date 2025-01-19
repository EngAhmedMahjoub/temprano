import os
from dotenv import load_dotenv
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import traceback

BOT_USERNAME: final = '@ttemprano_bot'

# Set your token using .env file
load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, I am your friendly assistant temprano! How can I help you?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Select the location for weather')

async def custom_command(update: Update, context: ContextTypes):
    await update.message.reply_text('Custom commands')

# Errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    traceback.print_exc()