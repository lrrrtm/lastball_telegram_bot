import sqlite3
import telebot
from constants import *
from buttons import *

bot = telebot.TeleBot(api)
db = sqlite3.connect(database, check_same_thread=False)
cur = db.cursor()
bot.send_message(mainAdmin, "Бот был перезагружен.")
markup = types.InlineKeyboardMarkup(row_width=1)
markup.add(button_23, button_24, button_25  , button_26, button_27)
bot.send_message(mainAdmin, "Выберите действие", reply_markup=markup)

cur.execute("select firstname, lastname, tID, ticketType, transferType from mainTable")
data = cur.fetchall()

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        tID = call.message.chat.id
        if call.data == "btn_23":
            for a in data:
                firstname, lastname, tID = a[0], a[1], a[2]
                try:
                    bot.send_message(tID, f"{firstname}, приветствуем тебя на Последнем Балу!"
                                          f"\n\nМы находимся на территории Малина Glamping. Во время проведения мероприятия *запрещено*:"
                                          f"\n- курение непосредственно в пределах Локации;"
                                          f"\n- употребление наркотических и (или) психотропных веществ;"
                                          f"\n- использование бассейна в целях, не соответствующими его прямому назначению;"
                                          f"\n- прыжки с бортиков бассейна;"
                                          f"\n- купание в водоёмах Локации (бассейне) в состоянии сильного алкогольного опьянения в тёмное время суток (с 24 часов до 06 часов следующих суток), оставление на открытой воде одного из участников мероприятия без надзора (контроля);"
                                          f"\n- агрессивное, провоцирующее поведение участников, наличие холодного или огнестрельного оружия и его демонстрацию участниками мероприятия другим участникам;"
                                          f"\n- пренебрежения участниками противопожарными нормами и правилами, правилами безопасного поведения на воде, правил обращения с фейерверками;"
                                          f"\n- порча имущества туристической базы."
                                          f"\n\n*Краткая программа мероприятия*"
                                          f"\n*14:00-16:00* - Meet&greet - легкие закуски и прохладительные напитки"
                                          f"\n*16:00-19:00* - Открытие бассейна и джакузи, подача основных блюд"
                                          f"\n*19:30-02:00* -  Концертная часть, дискотека"
                                          f"\n*02:00-02:30*  - Костер на пляже"
                                          f"\n\nЖелаем хорошо провести время с нами!\nЕсли возникают вопросы, задавай их организаторам, нахоядщимся на локации", parse_mode="Markdown")

                except Exception:
                    pass
            bot.send_message(mainAdmin, "Приветственные сообщения отправлены")
        if call.data == "btn_24":
            for a in data:
                firstname, lastname, tID = a[0], a[1], a[2]
                try:
                    bot.send_photo(tID, open(f"{rootSource}/map.png", "rb"), caption="Напоминаем о том, какие локации доступны на Последнем Балу")
                except Exception:
                    pass
            bot.send_message(mainAdmin, "Карта мероприятия отправлена")
        if call.data == "btn_25":
            for a in data:
                firstname, lastname, tID = a[0], a[1], a[2]
                try:
                    bot.send_message(tID, f"{firstname}, Последний Бал подходит к своему логическому завершению. Пожалуйста, не забывай свои личные вещи. Если ты видишь, что чья-то вещь осталась лежать без присмотра, сообщи об этом организаторам мероприятия."
                                          f"\n\nДля тех, кто оплачивал трансфер, информация будет предоставлена организаторами в ближайшее время."
                                          f"\n\nЭто было очень круто! Спасибо за участие в нашем мероприятии!"
                                          f"\nДо новых встреч 🤍")
                except Exception:
                    pass
            bot.send_message(mainAdmin, "Сообщения об окончании отправлены")
        if call.data == "btn_26":
            msg = bot.send_message(mainAdmin, "Отправь текст своего сообщения")
            bot.register_next_step_handler(msg, sendText)

        if call.data == "btn_27":
            msg = bot.send_message(mainAdmin, "Введи фамилию участника")
            bot.register_next_step_handler(msg, pickHuman)

def pickHuman(message):
    cur.execute(f"select tID, firstname, lastname, ticketType, transferType from mainTable where lastname = \"{message.text.capitalize()}\"")
    data = cur.fetchall()
    for a in data:
        tID, firstname, lastname, ticket, transfer = a[0], a[1], a[2], a[3], a[4]
    if len(data) != 0:
        bot.send_message(mainAdmin, f"{firstname} {lastname}\nБилет: {ticketTypes[ticket]}\nТрансфер: {transferTypes[transfer]}\ntID: {tID}")
    else:
        bot.send_message(mainAdmin, "Участник не найден. Попробуй ввести фамилию ещё раз, в ней может содержаться ошибка")
    try:
        bot.send_photo(mainAdmin, open(f"{path_userPhoto}{tID}.jpg", "rb"))
    except Exception as e:
        print(e)
        bot.send_message(mainAdmin, f"Фотография отсутсвует")
def sendText(message):
    text = message.text
    for a in data:
        firstname, lastname, tID = a[0], a[1], a[2]
        try:
            bot.send_message(tID, f"{text}")
        except Exception:
            pass
    bot.send_message(mainAdmin, f"Твоё сообщение отправлено\nТекст сообщения:\n{text}")
    showMenu(message)

@bot.message_handler(commands=['admin'])
def showMenu(message):
        tID = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(button_23, button_24, button_25, button_26, button_27)
        bot.send_message(tID, "Что отправить всем?", reply_markup=markup)

bot.polling(non_stop=True)