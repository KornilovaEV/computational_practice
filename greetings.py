import telebot
import json


# some functions to answer user's messages
def hello_out(bot, chat_id):
    msg = f'Hi!!!'
    hello_out = bot.send_message(chat_id, msg)
    return hello_out


def how_out(bot, chat_id):
    msg = f"I'm fine :)"
    how_out = bot.send_message(chat_id, msg)
    return how_out


def cute_out(bot, chat_id):
    msg = f"Thank you, it's nice of you"
    cute_out = bot.send_message(chat_id, msg)
    return cute_out


def lol_out(bot, chat_id):
    msg = f"Kek cheburek"
    lol_out = bot.send_message(chat_id, msg)
    return lol_out
