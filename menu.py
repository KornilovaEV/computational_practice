import telebot


# this function gives menu buttons
def main_menu(bot, chat_id):
    main_menu_buttons = telebot.types.ReplyKeyboardMarkup(row_width=1,
                                                          resize_keyboard=True)

    lol_button = telebot.types.KeyboardButton('Register')
    new_button = telebot.types.KeyboardButton('Send message')

    main_menu_buttons.add(lol_button, new_button)
    bot.send_message(chat_id, 'XD',
                     reply_markup=main_menu_buttons)
