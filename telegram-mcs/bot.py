# -*- coding: utf-8 -*-
import re
import config
from telebot import TeleBot, types

bot = TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажми меня", switch_inline_query="Telegram")
    keyboard.add(switch_button)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)

if __name__ == '__main__':
     bot.polling(none_stop=True)
