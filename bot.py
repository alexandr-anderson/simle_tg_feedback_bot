import time
import logging

from aiogram import Bot, Dispatcher, executor, types
import keyboard as kb

TOKEN = "5620535475:AAG9yymT-ehwyW_7TO4mexOiE1HXqTkOj9Y"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    mess = f'Привет, <b>{user_full_name}</b>'

    await message.reply(mess, parse_mode="html", reply_markup=kb.greet_kb)


@dp.message_handler(content_types=['text'])
async def user_text_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_first_name = message.from_user.first_name
    message_text = message.text
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    if message_text == "Привет":

        mess = f'И тебе привет <b>{user_first_name}</b>!'

    elif message_text == "Предложить новость":
        mess = f'Что бы предложить новость напишите ее прямо здесь или просто перешлите в данный чат, наши модераторы будут вам <b>{user_full_name}</b> крайне признательны и благодарны!)'

    elif message_text == "Сообщить об ошибке":
        mess = f'О любой ошибке можете написать прямо тут, в боте, заранее благодарю вас <b>{user_full_name}</b> за обратную связь и ваше участие!'

    elif message_text == "Нужна помощь?":
        mess = f'Выберете один из пунктов меню, затем опишите проблему или предложите новость, так же вы можете перейти к нам на сайт и оставит заявку менеджеру, с вами свяжутся в ближайшее время'

    elif message_text == "Веб сайт":
        mess = "Хотите перейти на сайт?, https://ligabarspb.ru/"

    else: mess = f'Сообщение получено и будет передано модератору, благодарю вас <i>{user_full_name}</i>'

    await message.reply(mess, parse_mode="html")


@dp.message_handler(content_types=['voice'])
async def user_voice_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_first_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    mess = f'Мммм  голосовое, отправляю его модератору и сам послушаю на досуге, спасибо тебе <b>{user_full_name}</b>!'

    await message.reply(mess, parse_mode="html")


@dp.message_handler(content_types=['video'])
async def user_video_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_first_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    mess = f'Ого настоящее видео, отправляю его модератору и сам посмотрю на досуге, спасибо тебе <b>{user_full_name}</b>!'

    await message.reply(mess, parse_mode="html")

@dp.message_handler(content_types=['photo'])
async def user_photo_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_first_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    mess = f'Крутое фото, отправляю его модератору, спасибо тебе <b>{user_full_name}</b>!'

    await message.reply(mess, parse_mode="html")


@dp.message_handler(content_types=['any'])
async def user_post_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_first_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    mess = f'Отличная новость, отправляю ее модератору, спасибо тебе <b>{user_full_name}</b>!'

    await message.reply(mess, parse_mode="html")


if __name__ == "__main__":
    executor.start_polling(dp)
