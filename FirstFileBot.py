import config
import telebot
from telebot import types
from time import sleep, time

bot = telebot.TeleBot(config.token)


def keyboard_kurs(calls):
    kb = types.InlineKeyboardMarkup()
    if calls == 'kurs':
        python = types.InlineKeyboardButton('Python', callback_data='pyth')
        grafdisn = types.InlineKeyboardButton('Графический дизайн', callback_data='grafdisn')
        mine = types.InlineKeyboardButton('Minecraft', callback_data='mine')
        robl = types.InlineKeyboardButton('Roblox', callback_data='robl')
        scr = types.InlineKeyboardButton('Scratch', callback_data='scr')
        kodu = types.InlineKeyboardButton('Kodu Game Lab', callback_data='kodu')

        kb.add(python, grafdisn)
        kb.add(scr, kodu)
        kb.add(mine, robl)
        return kb

    elif calls == 'formzap':
        zap = types.InlineKeyboardButton('Записаться на бесплатный урок', url=config.zapURL)
        oplat = types.InlineKeyboardButton('Купить курс онлайн', url=config.oplatURL)
        kb.add(zap)
        kb.add(oplat)
        return kb
    elif calls == 'FAQ':

        faq1 = types.InlineKeyboardButton('❓ С чего начать?', callback_data='faq1')
        faq2 = types.InlineKeyboardButton('❓ Что даст курс?', callback_data='faq2')
        faq3 = types.InlineKeyboardButton('❓ Не навредят ли занятия зрению или психике ребёнка?', callback_data='faq3')
        faq4 = types.InlineKeyboardButton('❓ В каком формате проходят занятия?', callback_data='faq4')
        faq5 = types.InlineKeyboardButton('❓ Какова стоимость занятий?', callback_data='faq5')
        kb.add(faq1)
        kb.add(faq2)
        kb.add(faq3)
        kb.add(faq4)
        kb.add(faq5)
        return kb
    elif calls == 'FAQback':
        back = types.InlineKeyboardButton("Назад", callback_data='FAQ')
        kb.add(back)
        return kb



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("О нас")
    but2 = types.KeyboardButton("Курсы")
    but3 = types.KeyboardButton("Лицензия")
    but4 = types.KeyboardButton("FAQ")
    but5 = types.KeyboardButton("Полезные боты")
    markup.add(but2, but4)
    markup.add(but1, but3)
    markup.add(but5)
    bot.send_photo(message.chat.id, photo=open(config.photo + 'logo.jpg', 'rb'),
                   caption=config.text_logo)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}\nВыберите что вас интересует в меню".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "Курсы":
        bot.send_photo(message.chat.id, photo=open(config.photo + 'kurs.png', 'rb'))
        bot.send_message(message.chat.id, text='Наши курсы:', reply_markup=keyboard_kurs("kurs"))
    elif message.text == "Лицензия":
        bot.send_photo(message.chat.id, photo=open(config.photo + 'licenz.jpg', 'rb'),
                       caption='Образовательная лицензия')
    elif message.text == "О нас":
        o_nasmarkup = types.InlineKeyboardMarkup()
        gruppa = types.InlineKeyboardButton('ВКонтакте', url=config.groupVK)
        site = types.InlineKeyboardButton('Официальный сайт', url=config.site)
        kont = types.InlineKeyboardButton('Контакты', callback_data='kont')

        o_nasmarkup.add(site, gruppa)
        o_nasmarkup.add(kont)
        bot.send_message(message.chat.id, config.o_nas, reply_markup=o_nasmarkup)
    elif message.text == "FAQ":
        bot.send_message(message.chat.id, "Часто задаваемые вопросы:", reply_markup=keyboard_kurs('FAQ'))
    elif message.text == "Полезные боты":
        botsmarkup = types.InlineKeyboardMarkup()
        bot1 = types.InlineKeyboardButton('Бот для важного', callback_data='botvazn')
        botsmarkup.add(bot1)
        bot.send_message(message.chat.id, "Наши боты:", reply_markup=botsmarkup)
    else:
        bot.send_message(message.chat.id, "Я не знаю что и ответить")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        # Курсы
        if call.data == "pyth":
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'python.png', 'rb'),
                           caption=config.kurs_pyth, reply_markup=keyboard_kurs('formzap'))
        elif call.data == "grafdisn":
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'graf.png', 'rb'),
                           caption=config.kurs_grafdisn, reply_markup=keyboard_kurs('formzap'))
        elif call.data == 'mine':
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'Minecraft.png', 'rb'),
                           caption=config.kurs_minecraft, reply_markup=keyboard_kurs('formzap'))
        elif call.data == 'robl':
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'roblox.png', 'rb'),
                           caption=config.kurs_roblox, reply_markup=keyboard_kurs('formzap'))
        elif call.data == 'scr':
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'Scratch.png', 'rb'),
                           caption=config.kurs_scratch, reply_markup=keyboard_kurs('formzap'))
        elif call.data == 'kodu':
            bot.send_photo(call.message.chat.id, photo=open(config.photo + 'Kodu.png', 'rb'),
                           caption=config.kurs_scratch, reply_markup=keyboard_kurs('formzap'))

        elif call.data == 'kont':
            o_nasmarkup = types.InlineKeyboardMarkup()
            gruppa = types.InlineKeyboardButton('ВКонтакте', url=config.groupVK)
            site = types.InlineKeyboardButton('Официальный сайт', url=config.site)

            o_nasmarkup.add(site, gruppa)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.kont,
                                  reply_markup=o_nasmarkup)
        #Часто задоваемые вопросы
        elif call.data == "FAQ":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Часто задаваемые вопросы:", reply_markup=keyboard_kurs('FAQ'))
        elif call.data == 'faq1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.faq1, reply_markup=keyboard_kurs('FAQback'))
        elif call.data == 'faq2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.faq2,
                                  reply_markup=keyboard_kurs('FAQback'))
        elif call.data == 'faq3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.faq3,
                                  reply_markup=keyboard_kurs('FAQback'))
        elif call.data == 'faq4':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.faq4,
                                  reply_markup=keyboard_kurs('FAQback'))
        elif call.data == 'faq5':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.faq5,
                                  reply_markup=keyboard_kurs('FAQback'))

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
