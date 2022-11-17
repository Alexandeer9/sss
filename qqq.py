from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
bot = Bot(token= '5650733079:AAGROZ5m3BtxYAnLbPlqdZeu-kKjzKPzSFg')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def Start(mes: types.Message):
    await mes.answer(text= f"Привет, {mes.from_user.first_name}!")




executor.start_polling(dp)

