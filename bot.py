import telebot
import config
from gtts import gTTS
import wis

#Инициализация бота
bot = telebot.TeleBot(config.token)

#Функция гугл бабы
@bot.message_handler(commands=['voice'], content_types=['text','audio'])
def textToVoice(msg):
    try:
        a = list(msg.text.split())
        del a[0]
        #Это я называю обработка исключений
        if len(a) == 0:
            bot.send_message(msg.chat.id, "Использование:\n/voice <текст> - голос в текст")
        else:
            text = ' '.join(a)
            #Само использование библиотеки gTTS
            tts = gTTS(text, lang="ru")
            #Файл постоянно перезаписывается, потому что нет необходимости
            #хранить аудиофайлы, да и это экономия памяти
            tts.save("result.ogg")
            voice = open('result.ogg', 'rb')
            #Отправка аудиофайла как голосового сообщения
            bot.send_voice(msg.chat.id, voice)
    except NameError:
        bot.send_message(msg.chat.id, "Whats get something wrong")

#Функция меню
@bot.message_handler(commands=['help'], content_types=['text'])
def menu(msg):
    try:
        #Да в коде это выглядит достаточно уродливо
        bot.send_message(msg.chat.id, "NKVD BOT ver. 0.1.4\n/help - команды\n/voice <text> - Гоголь баба\n/encode <текст> <ключ шифрования> - шифратор\n/decode <текст> <ключ шифрования> - дешифратор")
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

#По сути это тоже самое, что и "while True:" только оптимизировано под работу с Telegram Api
if __name__ == '__main__':
    bot.polling(none_stop=True)