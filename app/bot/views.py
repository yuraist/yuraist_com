import telebot
from . import bot
from .telegram_bot import telegram_bot, WEBHOOK_URL_PATH, WEBHOOK_URL_BASE
from flask import request, abort


@bot.route('/setWebhook')
def set_webhook():
    try:
        telegram_bot.remove_webhook()
        telegram_bot.set_webhook(WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
        return 'Webhook has been set up'
    except:
        return 'Webhook Error'


@bot.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        telegram_bot.process_new_updates([update])
        return ''
    else:
        return abort(403)
