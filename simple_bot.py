import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "8704652250:AAFGqPU5kE-3bth030Uy3MyclaboJdKCyDk"
dp = Dispatcher()

def main_menu():
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text="Asosiy"),
        KeyboardButton(text="Finans"),
        KeyboardButton(text="Mening malumotlarim"),
        KeyboardButton(text="Excel malumotlari"),
    )
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True)


@dp.message(F.text == '/start')
async def start_handler(message: Message):
    name = message.from_user.full_name
    await message.answer(
        f"Assalomu alaykum, {name}\nBotimiz sizga nima yordam bera oladi?",
        reply_markup=main_menu()
    )


@dp.message(F.text == "Asosiy")
async def asosiy(message: Message):
    await message.answer(" Asosiy menuga xush kelibsiz!", reply_markup=main_menu())


@dp.message(F.text == "Finans")
async def finans(message: Message):
    await message.answer(" Balansingiz: 1000 sum", reply_markup=main_menu())


@dp.message(F.text == "Mening malumotlarim")
async def mening_malumotlarim(message: Message):
    full_name = message.from_user.full_name
    username = message.from_user.username or "username yo'q"
    await message.answer(
        f" Sizning malumotlaringiz:\n\n"
        f"Ism: {full_name}\n"
        f"Username: @{username}",
        reply_markup=main_menu()
    )

@dp.message(F.text == "Excel malumotlari")
async def excel_malumotlari(message: Message):
    await message.answer(" Excel malumotlariga xush kelibsiz!", reply_markup=main_menu())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())