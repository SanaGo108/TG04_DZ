from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Обычная клавиатура с кнопками "Привет", "Пока", "/links", "/dynamic"
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
        [KeyboardButton(text="/links"), KeyboardButton(text="/dynamic")]
    ],
    resize_keyboard=True
)

# Инлайн-клавиатура с кнопками "Каталог", "Новости" и "Профиль"
inline_keyboard_test = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
        [InlineKeyboardButton(text="Новости", callback_data='news')],
        [InlineKeyboardButton(text="Профиль", callback_data='person')]
    ]
)

# Кнопки с URL-ссылками
links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url="https://news.ycombinator.com")],
        [InlineKeyboardButton(text="Музыка", url="https://music.youtube.com")],
        [InlineKeyboardButton(text="Видео", url="https://www.youtube.com")]
    ]
)

# Динамическая инлайн-клавиатура
dynamic_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ]
)

# Клавиатура с двумя опциями
options_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
    ]
)
