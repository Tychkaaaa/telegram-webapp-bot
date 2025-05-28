import telebot
from telebot.types import WebAppInfo, ReplyKeyboardMarkup

BOT_TOKEN = '7411865765:AAH5ImePdK2XlDDilsZzfqDSfgHI0IbP_nk'
WEBAPP_URL = 'https://your-project.onrender.com/'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['web_app_data'])
def handle_web_app_data(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"Ты отправил из WebApp:\n{data}")
"Добро пожаловать! Нажми кнопку:", reply_markup=markup

@bot.message_handler(content_types=["web_app_data"])
def handle_web_app(message):
    data = message.web_app_data.data
    bot.send_message(message.chat.id, f"Ты отправил из WebApp:\n\n{data}")

print("Бот запущен...")
bot.polling()