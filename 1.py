import config
import telebot as tb
from telebot import types

bot = tb.TeleBot(config.token)


a = types.InlineKeyboardMarkup()
a.add(types.InlineKeyboardButton("калькулятор", callback_data="calc"))

@bot.message_handler(content_types=["text"])
def calc(m):
        if call.data == "s_calc":
        def s_calc():
            bot.send_message(cmt, "Введите первое число:")
            @bot.message_handler(content_types=["text"])
            def f_num(m):
                x = int(m.text)
                return x
            bot.send_message(cmt, "Введите второе число:")
            @bot.message_handler(content_types=["text"])
            def s_num(m):
                y = int(m.text)
                return y
            bot.send_message(cmt, "Введите операцию:")
            @bot.message_handler(content_types=["text"])
            def oprtr(m):
                z = m.text
                return z
        return f_num(cmt), s_num(cmt), oprtr(cmt)
        bot.send_message(cmt, s_calc)


@bot.message_handler(commands=["start"])
def start_mess(m):
    mm = m.chat.id
    bot.send_message(mm, "hi")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cmt = call.message.chat.id
    if call.data == "calc":
        
            

if __name__ == "__main__":
    bot.infinity_polling()
