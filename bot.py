import json
import os.path
import config
import telebot
import menu
import greetings
import user
import random

# assign to variable value that allow to control bot
bot = telebot.TeleBot(config.TOKEN)


# handler of /start command
@bot.message_handler(commands=['start'])
def start_handler(message):
    msg = 'Hallo, nice to meet you'
    msg_out = bot.send_message(message.chat.id, msg)
    menu.main_menu(bot, message.chat.id)
    bot.send_sticker(message.chat.id,
                     'CAACAgIAAxkBAALkol7SyB5mKbDNttoXDpNTD9zihqqaAAK4AAPA-wgAAU2SSZjfsZSOGQQ')


# handler for user's commands
@bot.message_handler(content_types=['text'])
def text_handler(message):
    try:
        if hasattr(message.reply_to_message, 'text'):  # checks whether the message is a reply to another message
            msg = f'сообщение:' + message.reply_to_message.text + 'ответ: ' + message.text + f'Send me this number: {random.randint(0, 10)}'
            msg = message.reply_to_message.text.translate(coding("dec", int(message.text)))
            msg_out = bot.send_message(message.chat.id, msg)
        else:  # it goes if it's not a reply to a message
            if message.text == 'Hello':
                hello_out = greetings.hello_out(bot, message.chat.id)
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECGmdgXD9IAQdmC9xsEuaei6XMWSfbbgAC9QADe04qEEI1AAFASlpvZh4E')
            elif message.text == 'Register':
                global che
                che = random.randint(0, 10)
                msg = f'Send me this number: {che}'
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, ask_nick)
            elif message.text == 'How are you?':
                hello_out = greetings.how_out(bot, message.chat.id)
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECGmlgXEARqf8ZbQEBYBYAAcq8u81INxMAAhYCAALSxmEPqfUh5GhpX1EeBA')
            elif message.text == 'You are cute':
                hello_out = greetings.cute_out(bot, message.chat.id)
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECGmtgXEDM7Sg3Gu6eN8S0o3SbQ-n1wwACkwADE2MxBzpVc-VYZqd6HgQ')
            elif message.text == 'Lol':
                hello_out = greetings.lol_out(bot, message.chat.id)
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECGm9gXEEuEqJMA1HFkynenVnYssS3rgACSgADYmSaJFnWvDC0YiAHHgQ')
            elif message.text == 'Send message':
                msg = 'Enter message'
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, ask_who)
            else:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# function for asking user the recipient
def ask_who(message):
    try:
        mes = message.text
        if mes == '/Cancel' or mes == '/cancel':  # check if user wants to cancel operation
            msg = 'Sending canceled'
            msg_out = bot.send_message(message.chat.id, msg)
        else:
            global message_text
            message_text = mes
            msg = 'Enter recipient'
            msg_out = bot.send_message(message.chat.id, msg)
            bot.register_next_step_handler(msg_out, ask_code)
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# function for asking user the encrypting code
def ask_code(message):
    try:
        mes = message.text
        if mes == '/Cancel' or mes == '/cancel':  # check if user wants to cancel operation
            msg = 'Registration canceled'
            msg_out = bot.send_message(message.chat.id, msg)
        else:
            if user.nick_check(mes):  # check whether recipient nickname exists
                global recipient_id
                recipient_id = mes
                msg = 'Enter code'
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, send_message)
            else:
                msg = 'Recipient does not exist, enter enother nickname'
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, ask_code)
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# function for sending message
def send_message(message):
    try:
        mes = message.text
        if mes == '/Cancel' or mes == '/cancel':  # check if user wants to cancel operation
            msg = 'Sending canceled'
            msg_out = bot.send_message(message.chat.id, msg)
        elif not mes.isnumeric():  # checks whether the entered code is numeric
            msg = 'Code must be numeric int'
            msg_out = bot.send_message(message.chat.id, msg)
            bot.register_next_step_handler(msg_out, send_message)
        else:
            users = message.from_user.first_name
            msg = f'{message.chat.id}'
            file_user = f'.\\names\\{recipient_id}.json'
            newsa = "gg"
            msg_out = bot.send_message(message.chat.id, f'{recipient_id}')
            if os.path.exists(file_user):
                with open(file_user, 'r') as file:
                    f = json.load(file)
                newsa = f[3::]
            fik = f'.\\storage\\{message.chat.id}.json'
            if os.path.exists(fik):
                with open(fik, 'r') as file:
                    f = json.load(file)
            kek = f'Message from: {f}'
            msg_out = bot.send_message(int(newsa), message_text.translate(coding("enc", int(mes))))
            msg_out = bot.send_message(int(newsa), kek)
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# 1-st step of function for registration new user
def ask_nick(message):
    try:
        mes = message.text
        if mes == '/Cancel' or mes == '/cancel':  # check if user wants to cancel operation
            msg = 'Registration canceled'
            msg_out = bot.send_message(message.chat.id, msg)
        else:
            if mes.isnumeric() and int(mes) == che:  # check whether the entered code for registration is correct
                msg = "Create a nickname"
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, reg_new)
            else:
                msg = "You are wrong!"
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, ask_nick)
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# 2-nd step of function for registration new user
def reg_new(message):
    try:
        mes = message.text
        if mes == '/Cancel' or mes == '/cancel':  # check if user wants to cancel operation
            msg = 'Registration canceled'
            msg_out = bot.send_message(message.chat.id, msg)
        else:
            file_user = f'.\\names\\{mes}.json'
            file_cr = f'.\\storage\\{message.chat.id}.json'
            if os.path.exists(file_cr):  # checks whether the user has already registered
                msg = "You have already registered"
                msg_out = bot.send_message(message.chat.id, msg)
            elif os.path.exists(file_user):  # checks whether new user's nickname already exists
                msg = "Create another nickname"
                msg_out = bot.send_message(message.chat.id, msg)
                bot.register_next_step_handler(msg_out, reg_new)
            else:  # register user and add info to internal files
                f = f".\\names\\{mes}.json"
                with open(f, "w") as file:
                    json.dump(f'id: {message.chat.id}', file, indent=4, sort_keys=True)
                user.new_user(message.from_user.id, mes, message.chat.id
                              )
                users = message.from_user.first_name
                msg = f'{users}'
                msg_out = f'{msg}, You have successfully registered as {mes}'
                bot.send_message(message.chat.id, msg_out)
    except:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAECGpFgXFtHscdGzzVeKp7UIh-kVr6aMgACugADwPsIAAGSbw-9i6NJSx4E')


# creating alphabets for encrypting and decrypting messages
lower_cyrillic = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
upper_cyrillic = ''.join(map(chr, range(ord('А'), ord('Я') + 1)))
lower_eng = ''.join(map(chr, range(ord('a'), ord('z') + 1)))
upper_eng = ''.join(map(chr, range(ord('A'), ord('Z') + 1)))
lower_cyrillic = lower_cyrillic + lower_eng
upper_cyrillic = upper_cyrillic + upper_eng


# shifting alphabet on particular number
def alphabet(shift):
    return lower_cyrillic[shift:] + \
           lower_cyrillic[:shift] + \
           upper_cyrillic[shift:] + \
           upper_cyrillic[:shift]


# function for encrypting\decrypting message
def coding(typ="enc", shift=3):
    a1 = lower_cyrillic + upper_cyrillic
    a2 = alphabet(shift)

    t = {
        "enc": str.maketrans(a1, a2),
        "dec": str.maketrans(a2, a1)
    }

    return t[typ]


# always the last to run bot
bot.polling()
