# python -m pip install -r requirements.txt
api = "API-KEY-HERE"
rootSource = "SOURCE-HERE"

mainTable = "mainTable"
database = f"{rootSource}/lastball_db.db"
path_userQRC = f"{rootSource}/data/qrc/"
path_userPhoto = f"{rootSource}/data/photo/"
path_userSber = f'{rootSource}/data/sber/'
path_check = f'{rootSource}/data/check/'
path_userTicket = f'{rootSource}/data/ticket/'

ticketSource = f"{rootSource}/data/input_ticket.png"
mainAdmin = -721469452
admID = [-1001694517257, 409801981, 5523961510, 320518209]
startCode = "Q"
blacklist = [528329970]
ticketTypes = {0: "базовый", 1: "VIP"}
ticketCost = {0: 3700, 1: 5500}
transferTypes = {0: "только туда",1: "только обратно", 2: "туда и обратно", 3: "без трансфера"}
transferCost = {0: 500, 1: 500, 2: 1000, 3: 0}
nightHomeTypes = {0: "не включены", 1: "дом на двоих"}
nightHomeCost = {0: 0, 1: 6000}


errorA = "Что-то пошло не так. Попробуй отправить снова: "
errorM = "Возникла ошибка, сообщите её организаторам: "

alreadyEx = "Данный код регистрации уже был использован"


#НУЖНО ОТРЕДАКТИРОВАТЬ------------------------------------------------------------------------
startMessage = "Отправь мне свой пригласительный код"

welcomeText = ", приветствуем тебя на регистрации на *Последний Бал 2022!*"

infoText1 = "Вот и подошёл к концу невероятно долгий и одновременно короткий, но в то же время очень важный этап нашей жизни - гимназия остается позади." \
            "\nВ ней происходило множество веселых, интересных, грустных и волнующих моментов, которые отложились в наших сердцах навсегда." \
            "\n*Последний Бал* - это место, где мы в последний раз увидимся все вместе, встретим закат и рассвет, в последний раз вспомним всё, что происходило с нами, отдохнём и развлечемся после экзаменов, скажем друг другу все то, что так хотелось, но никак не находился нужный момент"

infoText2 = "Мероприятие будет проходить под открытым небом на берегу Балтийского моря в Зеленоградске." \
            "\n\n*Дата и время проведения: 14 июля, с 14:00 до рассвета.*" \
            "\n\nВ программе: торжественная концертная часть, вальс выпускников, фуршет, авторские коктейли, фейерверки, встреча рассвета на пляже у костров и многое другое"

infoText3 = "На карте мероприятия ты можешь увидеть разделение локации на различные зоны"

infoText4 = "Дресс-код для концертной части мероприятия - торжественный: костюм/смокинг, белая рубашка, галстук/бабочка или вечернее платье." \
            "\n\n*Дресс-код на торжественной части обязателен.*" \
            "\n\nПосле концертно-официальной части вы сможете переодеться в более свободную и комфортную одежду, но все равно не отходя от классического стиля." \
            "\n\nПри желании воспользоваться бассейном, на территории будет несколько комнат для переодевания в купальники и рядом с ними душевые кабинки"

infoText5 = "Вход на мероприятие платный и оплачивается заранее. На выбор доступны базовые и VIP билеты для прохода на мероприятие." \
            "\n\nСтоимость базового билета: *3700 рублей*" \
            "\n*Что входит:* возможность пользоваться всей доступной территорией, фуршет, авторские коктейли" \
            "\n\nСтоимость VIP билета: *5500 рублей*" \
            "\n*Что входит:* Все возможности базового билета + отдельная lounge зона с кальянами и индивидуальным обслуживанием" \
            "\n\nТакже за дополнительную плату в 500 рублей будет предоставлен трансфер до локации и за такую же цену трансфер обратно." \
            "\n\nПомимо этого, часть двухместных домиков на территории доступна для аренды на ночь за 6000 рублей" \
            "\n\n*Регистрация на мероприятие закрывается 29 июня*" \
            "\nС 29 июня для зарегистрировавшихся на мероприятие открывается оплата мероприятия." \
            "\n\nОплата закрывается *7 июля в 23:59*, после этого момента платежи приниматься не будут." \
            "\nВсем оплатившим придут их электронные билеты до 9 июля. Электронные билеты нужно будет предъявить на входе на мероприятие." \
            "\n\nТочный адрес и подробные правила мероприятия будут отправлены вместе с билетами." \
            "\n\nЕсли ты хочешь зарегистрироваться, нажми на кнопку ниже"

sendPhotoText = "Нам необходима одна твоя фотография для контроля, отправь её сюда. Обязательно отправляй своё фото, по нему тебя будут впускать на мероприятие."

recievedPhotoText = "Супер, фотография получена!"

waitingText = "Твоя заявка зарегистрирована, совсем скоро мы её обработаем и напишем тебе"

pickTicketText = "Выбери тип билета:\nБазовый (3700 ₽) или VIP (5500 ₽)"

pickHomeText = "Нужен ли домик на двоих? (6000 ₽)"

checkText = "Пора проверить всё перед тем, как отправить заявку"

transferTypeText = "Выбери тип трансфера"

areYouSureText = "Ты точно хочешь отменить заявку?"

ticketText = "*Информация о времени и месте*\n\nВстречаемся в бассейне гимназии №40 в 1:00\n\nУвидимся совсем скоро!❤"

#КОНЕЦ РЕДАКТИРОВАНИЯ------------------------------------------------------------------------

bankDetailsText1 = "твоя заявка подтверждена, для оплаты билета используй нужно перевести нужную сумму на одну из двух карт\n\n" \
                   "Сбербанк *4274320048249091* (София Александровна О.)\n\n" \
                   "Тинькофф Банк *2200700405219261* (Елизавета Александровна Л.)\n\n" \
                   "После успешного перевода нажми на кнопку ниже"

bankDetailsText2 = "твоя заявка подтверждена, для оплаты билета используй нужно перевести нужную сумму на одну из двух карт\n\n" \
                   "Сбербанк *4276200196230028* (Илья Андреевич Б.)\n\n" \
                   "Тинькофф Банк *2200700405219261* (Елизавета Александровна Л.)\n\n" \
                   "После успешного перевода нажми на кнопку ниже"

bankDetailsText3 = "твоя заявка подтверждена, для оплаты билета используй нужно перевести нужную сумму на одну из двух карт\n\n" \
                   "Сбербанк *2202202334822545* (Артём Александрович Л.)\n\n" \
                   "Тинькофф Банк *5536913999552520* (Всеволод Артемович В.)\n\n" \
                   "После успешного перевода нажми на кнопку ниже"

bankDetailsText4 = "твоя заявка подтверждена, для оплаты билета используй нужно перевести нужную сумму на одну из двух карт\n\n" \
                   "Сбербанк *5469980473717664* (Данил Витальевич П.)\n\n" \
                   "Тинькофф Банк *5536913999552520* (Всеволод Артемович В.)\n\n" \
                   "После успешного перевода нажми на кнопку ниже"


sendSberText = "Отправь мне скриншот из приложения банка, где будет видно, что перевод *действительно выполнен*"

recievedSberText = "Мы получили твой скриншот об оплате билета. После окончания приёма оплаты и обработки платежей мы оповестим тебя\nУвидимся на *Последнем Балу 2022!*"

cancelRegistrationText = "к сожалению сообщаем, что твоя заявка была отклонена"
