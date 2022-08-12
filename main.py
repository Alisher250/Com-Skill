from dispatcher import dp
from aiogram import executor
import bot

from db import BotDB
BotDB = BotDB('db/data.db')

if __name__ == '__main__':
    executor.start_polling(dp)
