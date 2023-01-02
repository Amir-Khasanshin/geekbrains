import telebot
import logging

logging.basicConfig( level = logging.INFO, filename = u'data.log', format="%(asctime)s %(levelname)s %(message)s", encoding='utf8')

bot=telebot.TeleBot("5915037820:AAEiA73sov73Fjda85xCPrhw2r0BAwI1Gik")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'напищи мне')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    logging.info(message.text)
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)