__all__ = [
  'register_message_handler'
]

import logging 
from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from db import async_session_maker, User

#настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#@dp.message(Command('start'))
async def help_command(message: types.Message):
    """справочная команда, регистрация пользователя"""
  
    async with async_session_maker() as session:
      session: AsyncSession
      query = select(User).where(User.user_id == message.from_user.id)
      user_exit = await session.exicute(query)

      if user_exit.scalar().all():
        await message.reply('Пользователь уже зарегистрирован')
        logging.info(f`user: {message.from_user.id}`)
      else:
        new_user = {
          'user_id': message.from_user.id,
          'username': message.from_user.username,
        }
        stmt = insert(User).values(**new_user)
        await session.execute(stmt)
        await session.commit()
        await message.reply('Пользователь зарегистрирован')
        logging.info(f`register new user: {message.from_user.id}`)


#@dp.message()
async def echo_command(message: types.Message):
    """Эхо-ответ"""
    await message.answer(message.text)
  logging.info(f`user{message.from_user.id} echoes {message.text}`))

def register_message_handler(router: Router):
  """Маршрутизация"""
  router.message.register(help_command, Command(commands = "start", "help"))
  router.message.register(echo_command, Command('echo'))

