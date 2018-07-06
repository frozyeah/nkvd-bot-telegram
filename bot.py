import telebot
import config
import wis

#Инициализация бота
bot = telebot.TeleBot(config.token)

#Функция меню
@bot.message_handler(commands=['help'], content_types=['text'])
def menu(msg):
    try:
        #Да в коде это выглядит достаточно уродливо
        bot.send_message(msg.chat.id, "NKVD BOT ver. 0.2\n/help - команды\n/huewords <text> - Хуефикатор\n/encode <текст> <ключ шифрования> - шифратор\n/decode <текст> <ключ шифрования> - дешифратор")
    except:
        bot.send_message(msg.chat.id, "Whats get something wrong")

#Шифратор Вижинера, чтобы узнать подробнее, посетите файл wis.py
@bot.message_handler(commands=['encode'], content_types=['text'])
def encode(msg):
    try:
        g = list(msg.text.split())
        if len(g) != 3:
            bot.send_message(msg.chat.id, "Использование:\n/encode <текст> <ключ>, - текст ТОЛЬКО латинскими буквами и БЕЗ пробелов, ключ используется для шифровки/дешифровки")
        else:
            inp = g[1]
            k = g[2]
            rez = wis.enc(inp, k)
            bot.send_message(msg.chat.id, rez)
    except:
        bot.send_message(msg.chat.id, "Whats get something wrong")

#Дешифратор Вижинера, чтобы узнать подробнее, посетите файл wis.py
@bot.message_handler(commands=['decode'], content_types=['text'])
def decode(msg):
    try:
        g = list(msg.text.split())
        if len(g) != 3:
            bot.send_message(msg.chat.id, "Использование:\n/decode <текст> <ключ>, - текст ТОЛЬКО латинскими буквами и БЕЗ пробелов, ключ используется для шифровки/дешифровки")
        else:
            inp = g[1]
            k = g[2]
            rez = wis.dec(inp, k)
            bot.send_message(msg.chat.id, rez)
    except:
        bot.send_message(msg.chat.id, "Whats get something wrong")

#Хуефикатор, давненько сделал, наконец то впихнул в бота
@bot.message_handler(commands=['huewords'], content_types=['text'])
def huewords(msg):
    a=list(msg.text.split())
    m=["а", "о", "е", "ё", "э", "у", "ю", "я", "и"]
    s={
        'я':"хуя",
        'а':"хуя",
        'о':"хуё",
        'ё':"хуё",
        'е':"хуе",
        'э':"хуе",
        'у':"хую",
        'ю':"хую",
        'и':"хуи"
    }
    r=""
    try:
        for n in a:
            if len(n)<4:
                r+=n+" "
            elif n[0] in m and n[2] == n[0]:
                r+=s[n[0]]+n[3::]+" "
            elif n[0] in m:
                r+=s[n[0]]+n[1::]+" "
            elif n[1] in m and n[3] == n[1]:
                r+=s[n[1]]+n[4::]+" "
            elif n[1] in m:
                r+=s[n[1]]+n[2::]+" "
            elif n[2] in m:
                r+=s[n[2]]+n[3::]+" "
            elif n[3] in m:
                r+=s[n[3]]+n[4::]+" "
            elif n[-1] in m:
                r+=s[n[-1]]+n[5::]+" "
        bot.send_message(msg.chat.id, r)
    except:
        bot.send_message(msg.chat.id, "Либо я криворукое чмо, либо ты пидар и юзаешь латиницу")

#По сути это тоже самое, что и "while True:" только оптимизировано под работу с Telegram Api
if __name__ == '__main__':
    bot.polling(none_stop=True)
