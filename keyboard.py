from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnReport = KeyboardButton ("Предложить новость")
btnBagReport = KeyboardButton ("Сообщить об ошибке")
btnHelp = KeyboardButton ("Нужна помощь?")
btnWebsite = KeyboardButton ("Веб сайт")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnReport, btnBagReport, btnWebsite, btnHelp)
