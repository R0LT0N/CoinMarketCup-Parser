from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import *
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InputMediaVideo
from aiogram.fsm.state import State, StatesGroup
import asyncio
import mysql.connector
from aiogram.enums import ParseMode
from playwright.async_api import async_playwright

router = Router()

bot = Bot(token="7776475378:AAGvyR_W48VT4rw7x3olFE10gkShwf0sc3w")

@router.message(Command("start"))
async def start_handler(message: Message):
    await bot.send_video(chat_id=message.from_user.id, video="https://i.imgur.com/qpgAyAo.mp4", caption="""
<b>
Привет! Ожидай, данные будут собираться каждые 3 часа
</b>
""", parse_mode=ParseMode.HTML)
    while True:
        await bot.send_message(message.from_user.id, "Топ 10 криптовалют, начинается парсинг...")

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            await page.goto('https://coinmarketcap.com/')

            await page.wait_for_selector('table.cmc-table')

            coins = await page.query_selector_all('table.cmc-table tbody tr')
            print(coins)
            abc = 0
            c = ""
            for coin in coins:
                abc+=1
                if abc == 11:
                    break
                symbol = await coin.query_selector('p.coin-item-symbol')
                symbol = await symbol.inner_text()
                name = await coin.query_selector('p.coin-item-name')
                name = await name.inner_text()
                price = await coin.query_selector('div.sc-b3fc6b7-0')
                price = await price.inner_text()
                h = await coin.query_selector('span.sc-a59753b0-0')
                h = await h.inner_text()
                volume = await coin.query_selector('p.bbHOdE')
                volume = await volume.inner_text()
                
                c += f"{abc}. {name} ({symbol}): {price}, 24h: {h}, Volume: {volume}\n"


        await bot.send_message(message.from_user.id, c)
        await asyncio.sleep(10800)