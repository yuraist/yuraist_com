import os
import logging
import telebot

# Bot config
API_TOKEN = os.environ.get('TOKEN')

WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'


WEBHOOK_URL_BASE = f'https://{WEBHOOK_HOST}:{WEBHOOK_PORT}'
WEBHOOK_URL_PATH = f'/{API_TOKEN}/'

# Logging setup
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

# Bot setup
telegram_bot = telebot.TeleBot(API_TOKEN)


# Bot handlers
@telegram_bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    telegram_bot.reply_to(message, "Hello, I'm an echo bot!")


@telegram_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    telegram_bot.reply_to(message, message.text)
