# Напишите Бота, удаляющего из текста все слова, содержащие "абв". (Ввод от пользователя)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# TOKEN = '5855468739:AAHTENF3PHYRfN-cH4wCPRf9wOcOoIcJN0A'

bot = Bot(token = '5855468739:AAHTENF3PHYRfN-cH4wCPRf9wOcOoIcJN0A')
updater = Updater(token = '5855468739:AAHTENF3PHYRfN-cH4wCPRf9wOcOoIcJN0A')
dispatcher = updater.dispatcher


def del_abv(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if 'абв' not in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(list1))

del_handler = MessageHandler(Filters.text, del_abv)

dispatcher.add_handler(del_handler)

updater.start_polling()
updater.idle()