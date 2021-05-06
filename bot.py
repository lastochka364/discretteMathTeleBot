import config
import telebot as tb
from telebot import types


bot = tb.TeleBot(config.token)


fnc = "Возможности бота:"
strt = "Здравствуй! Я - бот, который поможет Тебе в дискретной математике."
mtrls = "Доступны следующие материалы:"
help_txt = "В этом разделе доступна помощь от лучшего преподавателя ДМ - Кадомского Кирилла Константиновича!\nТакже доступны сайты для самообучения."
clc = "Этот калькулятор умеет делать различные вещи:"
tests = "Доступны следующие тесты:"
Lws_text = "В данном разделе доступны законы логики, множеств, операции над множествами, а так же их отображение на диаграммах Эйлера-Венна."


#InlineKeyboards.
st = types.InlineKeyboardMarkup()
st.add(types.InlineKeyboardButton("[Возможности бота]", callback_data="cpblts"))

cpbL = types.InlineKeyboardMarkup()
butt_m = types.InlineKeyboardButton("  [Материалы]  ", callback_data="mterials")
butt_h = types.InlineKeyboardButton("  [Помощь]  ", callback_data="helpp")
butt_c = types.InlineKeyboardButton("  [Калькулятор]  ", callback_data="calc")
butt_t = types.InlineKeyboardButton("  [Тесты]  ", callback_data="test")
cpbL.row(butt_m, butt_c)
cpbL.row(butt_h, butt_t)

mt = types.InlineKeyboardMarkup()
mt1 = types.InlineKeyboardButton(" [Книги] ", callback_data="book")
mt2 = types.InlineKeyboardButton(" [Лекции] ", callback_data="Lect")
mt3 = types.InlineKeyboardButton(" [Круги Эйлера-Венна Онлайн] ", url="http://www.reshim.su/blog/krugi_ehjlera/2016-07-04-681", callback_data="eyler")
mt4 = types.InlineKeyboardButton(" [Таблица истинности Онлайн] ", url="https://math.semestr.ru/inf/table.php", callback_data="truth_table")
mt5 = types.InlineKeyboardButton(" [Законы и диаграммы] ", callback_data="Laws_diag")
mt_back = types.InlineKeyboardButton("<---[Назад]", callback_data="mt_back")
mt.row(mt1, mt2)
mt.row(mt3, mt4)
mt.row(mt5)
mt.add(mt_back)

Laws = types.InlineKeyboardMarkup()
Lws1 = types.InlineKeyboardButton("Законы множеств", callback_data="set_logic")
Lws2 = types.InlineKeyboardButton("Законы логики", callback_data="logic")
Lws3 = types.InlineKeyboardButton("Операции над множествами", callback_data="operationset")
Lws4 = types.InlineKeyboardButton("Операции на диаграммах", callback_data="operationdiag")
Lws_back = types.InlineKeyboardButton("<---[Назад]", callback_data="Lws_back")
Laws.row(Lws1, Lws2)
Laws.row(Lws3, Lws4)
Laws.row(Lws_back)

opdiag = types.InlineKeyboardMarkup()
opd1 = types.InlineKeyboardButton("Перечесение", callback_data="intersection")
opd2 = types.InlineKeyboardButton("Обьединение", callback_data="union")
opd3 = types.InlineKeyboardButton("Вычитание", callback_data="substraction")
opd4 = types.InlineKeyboardButton("Симметрическая разность", callback_data="symm_diff")
opd_back = types.InlineKeyboardButton("<---[Назад]", callback_data="opd_back")
opdiag.row(opd1, opd2)
opdiag.row(opd3, opd4)
opdiag.row(opd_back)

bks = types.InlineKeyboardMarkup()
book1 = types.InlineKeyboardButton("Курс ДМ(Унив. 'ДУТ')", callback_data="b1")
book2 = types.InlineKeyboardButton("Теория графов(Унив. 'ДУТ')", callback_data="b2")
book3 = types.InlineKeyboardButton("Хаггарти ДМ для программистов", callback_data="b3")
book4 = types.InlineKeyboardButton("Тишин ДМ в примерах", callback_data="b4")
bks_back = types.InlineKeyboardButton("<---[Назад]", callback_data="bks_back")
bks.row(book1, book2)
bks.row(book3, book4)
bks.add(bks_back)

Lct = types.InlineKeyboardMarkup()
Lct1 = types.InlineKeyboardButton("Фомичев Лекция", callback_data="L1")
Lct2 = types.InlineKeyboardButton("Учебное пособие", callback_data="L2")
Lct3 = types.InlineKeyboardButton("Кулабухов Лекция", callback_data="L3")
Lct_back = types.InlineKeyboardButton("<---[Назад]", callback_data="Lct_back")
Lct.row(Lct1, Lct2)
Lct.row(Lct3)
Lct.add(Lct_back)

hllp = types.InlineKeyboardMarkup()
hllp.add(types.InlineKeyboardButton("Сайт К.К.К", url="https://sites.google.com/site/cyrilkadomsky/home", callback_data="hllp1"))
hllp.add(types.InlineKeyboardButton("<---[Назад]", callback_data="hllp_back"))

callc = types.InlineKeyboardMarkup()
callc1 = types.InlineKeyboardButton("[2 -> 10]", callback_data="c2_10")
callc2 = types.InlineKeyboardButton("[10 -> 2]", callback_data="c10_2")
callc3 = types.InlineKeyboardButton("[Обычный калькулятор]", callback_data="calculator")
callc_back = types.InlineKeyboardButton("<---[Назад]", callback_data="callc_back")
callc.row(callc1, callc2)
callc.row(callc3)
callc.add(callc_back)

tst = types.InlineKeyboardMarkup()
tst_sets = types.InlineKeyboardButton("Множества", callback_data="sets")

oprtn = types.InlineKeyboardMarkup()
op1 = types.InlineKeyboardButton("+", callback_data="+")
op2 = types.InlineKeyboardButton("-", callback_data="-")
op3 = types.InlineKeyboardButton("*", callback_data="*")
op4 = types.InlineKeyboardButton("/", callback_data="/")
oprtn.row(op1, op2)
oprtn.row(op3, op4)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    cmt = call.message.chat.id
    if call.data == "cpblts":
        bot.send_message(cmt, fnc, reply_markup=cpbL)
    if call.data == "mterials":
        bot.send_message(cmt, mtrls, reply_markup=mt)
    if call.data == "mt_back":
        bot.send_message(cmt, fnc, reply_markup=cpbL)
    if call.data == "book":
        bot.send_message(cmt, "Доступны следующие книги:", reply_markup=bks)
    if call.data == "b1":
        bot.send_document(cmt, open(r"books\Курс_ДМ(ДУТ).pdf", "rb"))
    if call.data == "b2":
        bot.send_document(cmt, open(r"books\Теория_графов(ДУТ).pdf", "rb"))
    if call.data == "b3":
        bot.send_document(cmt, open(r"books\Хаггарти_ДМ_для_программистов.pdf", "rb"))
    if call.data == "b4":
        bot.send_document(cmt, open(r"books\Тишин В.В. - Дискретная математика в примерах и задачах.pdf", "rb"))
    if call.data == "bks_back":
        bot.send_message(cmt, mtrls, reply_markup=mt)
    if call.data == "Lect":
        bot.send_message(cmt, "Доступны следующие лекции:", reply_markup=Lct)
    if call.data == "L1":
        bot.send_document(cmt, open(r"books\Фомичев_Лекция_ДМ.pdf", "rb"))
    if call.data == "L2":
        bot.send_document(cmt, open(r"books\Учебное_пособие_ДМ.pdf", "rb"))
    if call.data == "L3":
        bot.send_document(cmt, open(r"books\Кулабухов_Лекция.pdf", "rb"))
    if call.data == "Lct_back":
        bot.send_message(cmt, mtrls, reply_markup=mt)
    if call.data == "eyler":
        bot.send_message(cmt, "Круги Эйлера Онлайн", reply_markup=mt)
    if call.data == "thuth_table":
        bot.send_message(cmt, "Таблица истиноости Онлайн", reply_markup=mt)
    if call.data == "Laws_diag":
        bot.send_message(cmt, Lws_text, reply_markup=Laws)
    if call.data == "set_logic":
        bot.send_photo(cmt, open("photos\set_logic.png", "rb"))
    if call.data == "logic":
        bot.send_photo(cmt, open("photos\logic.png", "rb"))
    if call.data == "operationset":
        bot.send_photo(cmt, open("photos\operationsOnSets.png", "rb"))
    if call.data == "Lws_back":
        bot.send_message(cmt, mtrls, reply_markup=mt)
    if call.data == "operationdiag":
        bot.send_message(cmt, "Операции на диаграммах:", reply_markup=opdiag)
    if call.data == "union":
        bot.send_photo(cmt, open(r"photos\union.png", "rb"))
    if call.data == "intersection":
        bot.send_photo(cmt, open("photos\intersection.png", "rb"))
    if call.data == "substraction":
        bot.send_photo(cmt, open("photos\substraction.png", "rb"))
    if call.data == "symm_diff":
        bot.send_photo(cmt, open("photos\symm_diff.png", "rb"))
    if call.data == "opd_back":
        bot.send_message(cmt, Lws_text, reply_markup=Laws)
    if call.data == "helpp":
        bot.send_message(cmt, help_txt, reply_markup=hllp)
    if call.data == "hllp_back":
        bot.send_message(cmt, fnc, reply_markup=cpbL)
    if call.data == "calc":
        bot.send_message(cmt, clc, reply_markup=callc)
    if call.data == "callc_back":
        bot.send_message(cmt, fnc, reply_markup=cpbL)
    if call.data == "c10_2":
        bot.send_message(cmt, "Перевод из десятичной системы счсл. в двоичную.\nВведите число:")
        @bot.message_handler(content_types=["text"])
        def calc1(m):
            x = int(m.text)
            bot.send_message(cmt, format(x, "b"))
    if call.data == "c2_10":
        bot.send_message(cmt, "Перевод из двоичной системы счсл. в десятичную.\nВведите число:")
        @bot.message_handler(content_types=["text"])
        def calc2(m):
            x = m.text
            if "1" in x and "0" in x:
                bot.send_message(cmt, bin_to_dec(x))
            else:
                bot.send_message(cmt, "Введите двоичное число(прим. 1101)")


@bot.message_handler(commands=["start"])
def start_mess(m):
    mm = m.chat.id
    bot.send_message(mm, strt, reply_markup=st)


@bot.message_handler(commands=["help"])
def help_mess(m):
    mm = m.chat.id
    bot.send_message(mm, fnc, reply_markup=cpbL)


@bot.message_handler(commands=["m"])
def materials(m):
    mm = m.chat.id
    bot.send_message(mm, mtrls, reply_markup=mt)


@bot.message_handler(commands=["t"])
def tesst(m):
    mm = m.chat.id
    bot.send_message(mm, tests, reply_markup=tst)

@bot.message_handler(commands=["h"])
def help(m):
    mm = m.chat.id
    bot.send_message(mm, help_txt, reply_markup=hllp)


@bot.message_handler(commands=["c"])
def calc(m):
    mm = m.chat.id
    bot.send_message(mm, clc, reply_markup=callc)


def bin_to_dec(x):
    lenn = len(x)
    a = 0
    for i in range(0, lenn):
        a = a + int(x[i])*(2**(lenn-i-1))
    return a


def cllc(x, y, z):
    x = int(x)
    y = int(y)
    while True:
        if z == '0': break
        if z in ('+','-','*','/'):
            if z == '+':
                a = x + y
            elif z == '-':
                a = x - y
            elif z == '*':
                a = x * y
            elif z == '/':
                a = x // y
    return a


if __name__ == "__main__":
    bot.infinity_polling()

    
