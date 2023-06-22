import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from environs import Env


# Environmental variables
env = Env() 
env.read_env() 

translator = Translator()

API_TOKEN = env.str('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Google Tarjimon (EN-UZ, UZ-EN)")


@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'en'
    await message.reply(translator.translate(message.text, dest).text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)