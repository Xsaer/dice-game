from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep
from settings import API_KEY

bot = Bot(API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.username}! Начинаем игру!')
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'Вы проиграли!')
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, 'Вы победили!')
    else:
        await bot.send_message(message.from_user.id, 'Ничья!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
