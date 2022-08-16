import config
from dispatcher import dp
from aiogram.utils import executor
import bot

from db import BotDB
BotDB = BotDB(config.DB_URI)

if __name__ == '__main__':
    executor.start_polling(dp)
