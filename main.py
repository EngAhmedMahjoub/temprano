import os
from dotenv import load_dotenv
from typing import final

BOT_USERNAME: final = '@ttemprano_bot'

#set your token in .env file
load_dotenv()

TOKEN = os.getenv('TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')