import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand
from aiogram import F
from googletrans import Translator
from config import TOKEN
import keyboards as kb

# Настройка логирования
import logging
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

# Установка меню команд
async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/links", description="Показать ссылки"),
        BotCommand(command="/dynamic", description="Динамическое меню")
    ]
    await bot.set_my_commands(commands)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Выберите опцию:", reply_markup=kb.menu_keyboard)

# Обработчик команды /links
@dp.message(Command("links"))
async def show_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.links_keyboard)

# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def show_dynamic_keyboard(message: Message):
    await message.answer("Нажмите кнопку ниже:", reply_markup=kb.dynamic_keyboard)

# Обработчики кнопок "Привет" и "Пока"
@dp.message(F.text == "Привет")
async def greet_user(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(F.text == "Пока")
async def say_goodbye(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Обработчик нажатия кнопки "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_more_options(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=kb.options_keyboard)

# Обработчик нажатия кнопок "Опция 1" и "Опция 2"
@dp.callback_query(F.data == "option_1")
async def option_1_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опция 1")

@dp.callback_query(F.data == "option_2")
async def option_2_selected(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опция 2")

# Функция main
async def main():
    # Устанавливаем команды
    await set_bot_commands(bot)

    # Запускаем polling
    await dp.start_polling(bot)

# Запуск бота
if __name__ == '__main__':
    # Создаем новый цикл событий
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
