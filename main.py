import telebot
bot = telebot.TeleBot('5650733079:AAGROZ5m3BtxYAnLbPlqdZeu-kKjzKPzSFg')

@bot.message_handler(commands= ["start"])
def start(message):
    bot.send_message(message.chat.id, "<b>Бот</b> запущен успешно!", parse_mode="HTML")

@bot.message_handler(content_types= ["text"])
def nast(message):
    if message.text == "Как дела?":
        bot.send_message(message.chat.id, "иди лесом")
    else:
        bot.send_message(message.chat.id, "я тебя не понимаю")

@bot.message_handler(content_types= ["photo"])
def get_photo(message):
    bot.send_message(message.chat.id, "Крутое фото!")

@bot.message_handler(content_types= ["audio"])
def get_photo(message):
    bot.send_message(message.chat.id, "Крутое трекк!")






bot.polling(non_stop=True)

