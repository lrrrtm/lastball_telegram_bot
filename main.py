import sqlite3
from PIL import Image, ImageDraw, ImageFont
import telebot
import re
import qrcode
from constants import *
from buttons import *

bot = telebot.TeleBot(api)
db = sqlite3.connect(database, check_same_thread=False)
cur = db.cursor()

@bot.message_handler(commands=['send'])
def sendTicket(message):
    countSent = countNotSent =0
    if int(message.chat.id) in admID:
        cur.execute("select * from mainTable where isDonated = 1")
        data = cur.fetchall()
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(button_21)
        for a in range(len(data)):
            try:
                bot.send_message(data[a][0], f"{data[a][1]}, твой платёж успешно обработан!\nЧтобы получить билет, нажми на кнопку ниже", reply_markup=markup, parse_mode="Markdown")
                countSent += 1
            except Exception as e:
                bot.send_message(mainAdmin, f"Не удалось отправить билет {data[a][0]}\n{str(e)}")
                countNotSent += 1
        bot.send_message(message.chat.id, f"Всего: {len(data)}\nОтправлено: {countSent}\nНе удалось отправить: {countNotSent}")

@bot.message_handler(commands=['get'])
def getTable(message):
    if int(message.chat.id) in admID:
        bot.send_document(message.chat.id,open(database, "rb"))

@bot.message_handler(commands=['notify'])
def getNotify(message):
    if int(message.chat.id) in admID:
        msg = bot.send_message(message.chat.id, "Отправьте .txt с сообщением", parse_mode="Markdown")
        bot.register_next_step_handler(msg, sendNotify)

def sendNotify(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = rootSource + "/notify.txt"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Данные получены")

    cur.execute("select tID from mainTable")
    data = cur.fetchall()
    dataText= open(rootSource + "/notify.txt", "r", encoding="utf-8").readlines()
    text = ""
    for a in dataText:
        text = text + a
    for a in data:
        try:
            bot.send_message(a[0], f"*СООБЩЕНИЕ ОТ ОРГАНИЗАТОРОВ*\n\n{text}", parse_mode="Markdown")
        except Exception:
            pass
    bot.send_message(message.chat.id, "Уведомления отправлены", parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startMessage, parse_mode="Markdown")

@bot.message_handler(commands=['data'])
def getData(message):
    text = ""
    summ = 0
    count = 0
    if int(message.chat.id) in admID:
            cur.execute(f"select firstname, lastname, cost from mainTable where status = 1")
            data = cur.fetchall()
            for a in range(len(data)):
                    try:
                        count +=1
                        line = str(data[a][0]) + " " + str(data[a][1]) + " " + str(data[a][2]) + "₽" + "\n"
                        summ += int(data[a][2])
                        print(summ)
                        text += line
                    except Exception as e:
                        bot.send_message(message.chat.id, str(e), parse_mode="Markdown")
            bot.send_message(message.chat.id, text, parse_mode="Markdown")
            bot.send_message(message.chat.id, f"Зарегистрировано: {count}/{len(data)}\nОбщая сумма: {summ} ₽", parse_mode="Markdown")

@bot.message_handler(commands=['update'])
def update(message):
    if int(message.chat.id) in admID:
        cur.execute('select tID, firstname, lastname, status from mainTable')
        data = cur.fetchall()
        countRegTrue = 0
        countRegFalse = 0
        for x in range(0,21):
            a = data[x]
            if a[3] == 2:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_22)
                try:
                    bot.send_message(a[0], f"{a[1]}, {bankDetailsText1}", reply_markup=markup, parse_mode="Markdown")
                except Exception:
                    pass
                countRegTrue += 1

            elif a[3] == 3:
                try:
                    bot.send_message(a[0], f"{a[1]}, {cancelRegistrationText}", parse_mode="Markdown")
                except Exception:
                    pass
                countRegFalse += 1
        for x in range(21,43):
            a = data[x]
            if a[3] == 2:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_22)
                try:
                    bot.send_message(a[0], f"{a[1]}, {bankDetailsText2}", reply_markup=markup, parse_mode="Markdown")
                except Exception:
                    pass
                countRegTrue += 1

            elif a[3] == 3:
                try:
                    bot.send_message(a[0], f"{a[1]}, {cancelRegistrationText}", parse_mode="Markdown")
                except Exception:
                    pass
                countRegFalse += 1
        for x in range(43,64):
            a = data[x]
            if a[3] == 2:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_22)
                try:
                    bot.send_message(a[0], f"{a[1]}, {bankDetailsText3}", reply_markup=markup, parse_mode="Markdown")
                except Exception:
                    pass
                countRegTrue += 1

            elif a[3] == 3:
                try:
                    bot.send_message(a[0], f"{a[1]}, {cancelRegistrationText}", parse_mode="Markdown")
                except Exception:
                    pass
                countRegFalse += 1
        for x in range(64,len(data)):
            a = data[x]
            if a[3] == 2:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_22)
                try:
                    bot.send_message(a[0], f"{a[1]}, {bankDetailsText4}", reply_markup=markup, parse_mode="Markdown")
                except Exception:
                    pass
                countRegTrue += 1

            elif a[3] == 3:
                try:
                    bot.send_message(a[0], f"{a[1]}, {cancelRegistrationText}", parse_mode="Markdown")
                except Exception:
                    pass
                countRegFalse += 1
        bot.send_message(message.chat.id, f"Всего: {len(data)}\nОтправлено: {countRegFalse+countRegTrue}/{len(data)}\nПодтверждено: {countRegTrue}\nОтклонено: {countRegFalse}", parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        tID = call.message.chat.id
        if call.data == "btn_1": #пересылка на текст 2
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_2)
            bot.send_video(tID, open(f"{rootSource}/promo.mp4", 'rb'), width=1920, height=1080)
            bot.send_message(tID, infoText2, parse_mode="Markdown", reply_markup=markup)

        if call.data == "btn_2": #пересылка на текст 3
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_3)
            bot.send_photo(tID, open(f"{rootSource}/map.png", "rb"), infoText3, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_3": #пересылка на текст 4
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_4)
            bot.send_photo(tID, open(f"{rootSource}/location.jpg", "rb"), infoText4, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_4": #пересылка на текст 5
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_5)
            bot.send_message(tID, infoText5, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_5": #пересылка на отправку фото
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            msg = bot.send_message(tID, sendPhotoText, parse_mode="Markdown")
            bot.register_next_step_handler(msg, photo)

        if call.data == "btn_6":  # пересылка на выбор трансфера для базового уровня
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set ticketType = 0 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_10, button_11, button_12, button_17)
            bot.send_message(tID, transferTypeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_7":  # пересылка на выбор домика на ночь для випа
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set ticketType = 1 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_10, button_11, button_12, button_17)
            bot.send_message(tID, transferTypeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_8":  # пересылка на финальную сумму
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set nightHome = 1 where tID = \"{tID}\"")
            db.commit()
            checkAll(call.message)

        if call.data == "btn_9":  # пересылка на финальную сумму
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set nightHome = 0 where tID = \"{tID}\"")
            db.commit()
            checkAll(call.message)

        if call.data == "btn_10":  # пересылка на выбор домика на ночь для базового
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set transferType = 0 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_15, button_16)
            bot.send_message(tID, pickHomeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_11":  # пересылка на выбор домика на ночь для базового
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set transferType = 1 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_15, button_16)
            bot.send_message(tID, pickHomeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_12":  # пересылка на выбор домика на ночь для базового
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set transferType = 2 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_15, button_16)
            bot.send_message(tID, pickHomeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_17":  # пересылка на выбор домика на ночь для базового
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set transferType = 3 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_15, button_16)
            bot.send_message(tID, pickHomeText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_13":  # сохранение заявки
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set status = 1 where tID = \"{tID}\"")
            db.commit()
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_14)
            cur.execute(f"select * from mainTable where tID = \"{tID}\"")
            data = cur.fetchall()[0]
            firstname, lastname, ticketType, transferType, nightHome = str(data[1]), data[2], ticketTypes[int(data[3])], \
                                                                       transferTypes[int(data[4])], nightHomeTypes[int(data[5])]
            summ = ticketCost[int(data[3])] + transferCost[int(data[4])] + nightHomeCost[int(data[5])]
            if nightHome == "1": summ += 8000
            text = f"Имя: *{firstname} {lastname}*\nТип билета: *{ticketType}*\nТип трансфера: *{transferType}*" \
                   f"\nДополнительные услуги: *{nightHome}*\nИтоговая сумма: *{summ} ₽ *"
            text = waitingText + f"\n\nИнформация о заявке\n{text}"
            cur.execute(f"update mainTable set cost = {summ} where tID = \"{tID}\"")
            db.commit()

            bot.send_message(tID, text,reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_14":  # удаление заявки
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            cur.execute(f"select status, firstname from mainTable where tID = \"{tID}\"")
            data = cur.fetchall()[0]
            if data[0] > 3:
                bot.send_message(tID, f"{data[1]}, заявку невозможно отменить, твой платёж уже обрабатывается.\nЕсли возникла проблема, сообщи о ней организаторам, передав *свой код регистрации: {tID}*", parse_mode="Markdown")
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_19, button_20)
                bot.send_message(tID, areYouSureText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_19":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set isLinkTapped = 0 where tID = \"{tID}\"")
            cur.execute(f"update mainTable set status = 0 where tID = \"{tID}\"")
            db.commit()
            bot.send_message(tID, "Твоя заявка удалена. Если ты вновь захочешь к нам присоединиться, "
                                  "просто отправь свой пригласительный код ещё раз \n\n*ВНИМАНИЕ\nПередача своего пригласительного кода другому человеку строго запрещена!*",
                             parse_mode="Markdown")

        if call.data == "btn_20":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"select status from mainTable where tID = \"{tID}\"")
            data = cur.fetchall()[0]
            if data[0] == 2:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_22)
                bot.send_message(tID, bankDetailsText, reply_markup=markup, parse_mode="Markdown")
            else:
                cur.execute(f"select * from mainTable where tID = \"{tID}\"")
                data = cur.fetchall()[0]
                firstname, lastname, ticketType, transferType, nightHome = str(data[1]), data[2], ticketTypes[int(data[3])], \
                                                                           transferTypes[int(data[4])], nightHomeTypes[int(data[5])]
                summ = ticketCost[int(data[3])] + transferCost[int(data[4])] + nightHomeCost[int(data[5])]
                text = f"Имя: *{firstname} {lastname}*\nТип билета: *{ticketType}*\nТип трансфера: *{transferType}*" \
                       f"\nДополнительные услуги: *{nightHome}*\nИтоговая сумма: *{summ} ₽ *"
                text = waitingText + f"\n\nИнформация о заявке\n{text}"
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(button_14)
                bot.send_message(tID, text, reply_markup=markup, parse_mode="Markdown")


        if call.data == "btn_15":  # сохранение заявки
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set nightHome = \"1\" where tID = \"{tID}\"")
            db.commit()
            checkAll(call.message)

        if call.data == "btn_16":  # сохранение заявки
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"update mainTable set nightHome = \"0\" where tID = \"{tID}\"")
            db.commit()
            checkAll(call.message)

        if call.data == "btn_18":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(button_6, button_7)
            bot.send_message(tID, pickTicketText, reply_markup=markup, parse_mode="Markdown")

        if call.data == "btn_21":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            cur.execute(f"select firstname, lastname, tID, ticketType, transferType from mainTable where tID = \"{tID}\"")
            data = cur.fetchall()
            getTicket(data[0][0], data[0][1], data[0][2], ticketTypes[int(data[0][3])], transferTypes[int(data[0][4])])
            bot.send_message(tID, ticketText, parse_mode = "Markdown")
            bot.send_document(tID, open(path_userTicket + f"ticket{tID}.png", 'rb'))

        if call.data == "btn_22":
            bot.edit_message_reply_markup(tID, call.message.message_id, reply_markup=None)
            msg = bot.send_message(tID, sendSberText, parse_mode="Markdown")
            bot.register_next_step_handler(msg, sberPhoto)

@bot.message_handler(commands=['black'])
def black(message):
    if int(message.chat.id) in admID:
        msg = bot.send_message(message.chat.id, "Отправьте tID")
        bot.register_next_step_handler(msg, black2)
def black2(message):
    try:
        blacklist.append(int(message.text))
        bot.send_message(message.chat.id, f"Пользователь {message.text} добавлен в чёрный список")
    except Exception as e:
        bot.send_message(message.chat.id, errorA + str(e))

@bot.message_handler(content_types=['text'])
def checkCode(message):
    tID = message.chat.id
    if int(tID) not in blacklist:
        try:
            if re.match(startCode, message.text):
                cur.execute(f"select firstname, isLinkTapped from mainTable where key = \"{message.text}\"")
                data = cur.fetchall()[0]
                if data[1] == 1:
                    bot.send_message(tID, alreadyEx, parse_mode="Markdown")
                else:
                    cur.execute(f"update mainTable set isLinkTapped = 1 where key = \"{message.text}\"")
                    db.commit()
                    cur.execute(f"update mainTable set tID = \"{message.chat.id}\" where key = \"{message.text}\"")
                    db.commit()

                    bot.send_message(tID, data[0] + welcomeText, parse_mode="Markdown")
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    markup.add(button_1)
                    bot.send_message(tID, infoText1, reply_markup=markup, parse_mode="Markdown")

        except Exception as e:
            bot.send_message(mainAdmin, f"Ошибка у пользователя {tID} при вводе кода регистрации: {str(e)}", parse_mode="Markdown")
    else:
        bot.send_message(tID, "Вы были внесены в чёрный список")

def photo(message):
    tID = message.chat.id
    try:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        photoName = str(message.chat.id) + ".jpg"
        src = path_userPhoto + photoName
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, recievedPhotoText, parse_mode="Markdown")
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(button_6, button_7)
        bot.send_message(tID, pickTicketText, reply_markup=markup, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(mainAdmin, f"Ошибка у пользователя {tID} при отправке своей фотографии: {str(e)}", parse_mode="Markdown")
        msg = bot.send_message(message.chat.id, errorA, parse_mode="Markdown")
        bot.register_next_step_handler(msg, photo)

def sberPhoto(message):
    tID = message.chat.id
    try:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        photoName = str(tID) + ".png"
        src = path_userSber + photoName
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(tID, recievedSberText, parse_mode="Markdown")
        cur.execute(f"update mainTable set status = \"4\" where tID = \"{tID}\"")
        db.commit()

    except Exception as e:
        bot.send_message(mainAdmin, f"Ошибка у пользователя {tID} при отправке скриншота: {str(e)}", parse_mode="Markdown")
        msg = bot.send_message(message.chat.id, errorA, parse_mode="Markdown")
        bot.register_next_step_handler(msg, photo)

def checkAll(message):
    tID = message.chat.id
    cur.execute(f"select * from mainTable where tID = \"{tID}\"")
    data = cur.fetchall()[0]
    #print(data[1], data[2], str(data[3]), str(data[4]), transferTypes[int(data[4])])
    firstname, lastname, ticketType, transferType, nightHome = data[1], data[2], ticketTypes[int(data[3])], \
                                                               transferTypes[int(data[4])], nightHomeTypes[int(data[5])]
    summ = ticketCost[int(data[3])] + transferCost[int(data[4])] + nightHomeCost[int(data[5])]
    text = f"Имя: *{firstname} {lastname}*\nТип билета: *{ticketType}*\nТип трансфера: *{transferType}*" \
           f"\nДополнительные услуги: *{nightHome}*\nИтоговая сумма: *{summ} ₽*"
    text = checkText + "\n\n" + text
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(button_13, button_18, button_14)
    bot.send_message(tID, text, parse_mode="Markdown", reply_markup=markup)

def getTicket(firstname, lastname, tID, ticketType, transferType):
    try:
        ticket = Image.open(ticketSource)
        idraw = ImageDraw.Draw(ticket)
        font_size1 = 200
        font_size2 = 120
        font1 = ImageFont.truetype(f"{rootSource}/Architectural.ttf", size=font_size1)
        font2 = ImageFont.truetype(f"{rootSource}/Architectural.ttf", size=font_size2)
        idraw.text((165, 1135), firstname, font=font1, fill=(229, 233, 199), stroke_width=1)
        idraw.text((165+350, 1135), lastname, font=font1, fill=(229, 233, 199), stroke_width=1)
        idraw.text((168, 1310), f"Категория билета: {ticketType}", font=font2, fill=(229, 233, 199), stroke_width=1)
        idraw.text((168, 1422), f"Трансфер: {transferType}", font=font2, fill=(229, 233, 199), stroke_width=1)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=18,
            border=0,
        )
        qr.add_data(str(tID))
        qr.make(fit=True)
        img = qr.make_image(back_color="#ffffff", fill_color=(26, 38, 106))
        img.save(path_userQRC + 'qrcode' + str(tID) + '.png')
        img = Image.open(path_userQRC + 'qrcode' + str(tID) + '.png')
        img = img.convert("RGBA")
        mainData = img.getdata()
        newData = []
        for item in mainData:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(path_userQRC + 'qrcode' + str(tID) + '.png', "PNG")
        watermark = Image.open(
            path_userQRC + 'qrcode' + str(tID) + '.png')
        ticket.paste(watermark, (2665, 1020), mask=watermark)
        ticket.save(path_userTicket + 'ticket' + str(tID) + '.png')

    except Exception as e:
        print(e)

bot.polling(non_stop=True)