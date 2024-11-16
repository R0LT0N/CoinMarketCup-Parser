from playwright.sync_api import sync_playwright
from colorama import Fore
from aiogram import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from start import start
import asyncio
import logging

print (Fore.GREEN + """
██████╗░░█████╗░████████╗  ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝
██████╦╝██║░░██║░░░██║░░░  ██████╔╝█████╗░░███████║██║░░██║░╚████╔╝░
██╔══██╗██║░░██║░░░██║░░░  ██╔══██╗██╔══╝░░██╔══██║██║░░██║░░╚██╔╝░░
██████╦╝╚█████╔╝░░░██║░░░  ██║░░██║███████╗██║░░██║██████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░
""")


bot = Bot(token="7776475378:AAGvyR_W48VT4rw7x3olFE10gkShwf0sc3w")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(start.router)

logging.basicConfig(level=logging.INFO)

async def init_main ():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(init_main())