# Установить библиотеки и фреймворки aiogram==3.4
# pip install aiogram
# pip install python-dotenv
# pip install sqlalchemy
# pip install aiosqlite

# Для сохранения текущих пакетов в проекте и их версий при переносе используйте файл requirements.txt
# pip freeze — внешние пакеты проекта
# pip freeze > requirements.txt — сохранить внешние пакеты в файл
# pip install -r requirements.txt —  загрузить пакеты из файла

import logging #библиотека логирования (журналирования)
import asyncio # библиотека для асинхронного программирования
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers import register_message_handler



#асинхронный вызов функции - конкурентный вызов с ожиданием события для продолжения процесса выполнения 

@dp.message(Command('start'))
async def process_start_message(message:types. Message):
    """Привествие"""
    await message.answer('Привет!')

@dp.message()
async def echo(message: types.Message):
    """Эхо-ответ"""
    await message.answer(message.text)


async def main():
    """Настройки перед запуском бота"""

    #уровень логирования
    logging.basicConfig(level=logging.DEBUG)
    
    #создание экземпляров классов Bot и Dispatcher
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    #функция для вызова хендлеров из пакета handles
    register_message_handler(dp)
    
    await dp.start_polling (bot)

if __name__ == "__main__":
    #обработка исключений try-except
    try:
        asyncio.run(start())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Пока!")
    



























