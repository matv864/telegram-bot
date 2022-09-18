import telebot
from telebot import types

token = ""
bot = telebot.TeleBot(token)



information = []

repl_message = '''это такой-то текст, то-то, то-то нажми на кнопку, если готов начать'''


markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
item1=types.KeyboardButton("/start")
markup.add(item1)  


def result_func(inf):
    if inf == ["мужской", "тошнота", "желтуха", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат ГЕПАТИТ С , примерная стоимость экспресс теста начинается с 105 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["мужской", "боль в суставах", "потемнение мочи", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат ГЕПАТИТ Б, примерная стоимость экспресс теста начинается с 244 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение."""

    elif inf == ["мужской", "кровохарканье", "температура до 37.5", "контактировал с людьми болеющими туберкулёзом"]:
        return """Ваш возможный результат туберкулёз , примерная стоимость экспресс теста начинается с 199 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["мужской", "ноющие или схватывающие боли в зоне живота", "изжога", "неожиданные боли в желудке"]:
        return """Ваш возможный результат гастрит  , примерная стоимость экспресс теста начинается с 240 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["мужской", "патологические выделения из уретры", "увеличение местных лимфатических узлов", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат сифилис , примерная стоимость экспресс теста начинается с 199 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""


    elif inf[:3] == ["женский", "тошнота", "задержка менструации"]:
        return """Ваш результат, возможные симптомы указывают на беременность. Вы можете приобрести тест на определение беременности в любой аптеке и провести анализ. Примерный диапазон цены от 150 рублей до 1000 рублей , все зависит от проживания вашего региона , а так же формата тестов ( тест полоска,электронный).
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение."""

    elif inf == ["женский", "боль в суставах", "высыпания", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат ГЕПАТИТ Б, примерная стоимость экспресс теста начинается с 244 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение."""

    elif inf == ["женский", "обесцвечивание кала", "потемнение мочи", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат ГЕПАТИТ C , примерная стоимость экспресс теста начинается с 105 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["женский", "ноющие или схватывающие боли в зоне живота", "изжога", "неожиданные боли в желудке"]:
        return """Ваш возможный результат гастрит  , примерная стоимость экспресс теста начинается с 240 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["женский", "кровохарканье", "температура до 37.5", "контактировал с людьми болеющими туберкулёзом"]:
        return """Ваш возможный результат туберкулёз , примерная стоимость экспресс теста начинается с 199 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""

    elif inf == ["женский", "сильный зуд и жжение в области влагалища", "вязкие желтовато - белые выделения из влагалища с неприятным запахом", "был совершен незащищённый ПА"]:
        return """Ваш возможный результат сифилис , примерная стоимость экспресс теста начинается с 199 рублей. Его возможно приобрести в любой аптеке 
Данный тест несёт ознакомление и возможные болезни, при положительном результате теста незамедлительно обратитесь ко врачу.
Если данный тест показал отрицательный результат, но ваши симптомы сохранились в течение короткого срока времени , просим незамедлительно обратиться ко врачу чтобы поставили верный диагноз болезни и назначали верное лечение"""



    return "Ваши симптомы не подходят под болезни в нашей базе, поэтому просим обратиться к специалистам для уточнения диагноза и формы лечения"



@bot.message_handler(commands=['start'])
def start_message(message):
    global information
    information = []
    bot.send_message(message.from_user.id, repl_message, reply_markup = markup)
    bot.register_next_step_handler(message, main_question)



def main_question(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("мужской")
    item2=types.KeyboardButton("женский")
    markup.add(item1)
    markup.add(item2)
    
    if (message.text == "/start"):
        bot.send_message(message.from_user.id, "тогда первый вопрос")

        bot.send_message(message.from_user.id, "укажите свой пол", reply_markup = markup)
        bot.register_next_step_handler(message, fork)

def fork(message):
    global information

    if (message.text == "мужской"):
        information.append(message.text)
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("тошнота")
        item2=types.KeyboardButton("боль в суставах")
        item3=types.KeyboardButton("ноющие или схватывающие боли в зоне живота")
        item4=types.KeyboardButton("кровохарканье")
        item5=types.KeyboardButton("патологические выделения из уретры")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)   

        bot.send_message(message.from_user.id, "какие симптомы вас беспокоят?", reply_markup=markup)
        bot.register_next_step_handler(message, male1)
    elif (message.text == "женский"):
        information.append(message.text)
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("тошнота")
        item2=types.KeyboardButton("боль в суставах")
        item3=types.KeyboardButton("обесцвечивание кала")
        item4=types.KeyboardButton("ноющие или схватывающие боли в зоне живота")
        item5=types.KeyboardButton("кровохарканье")
        item6=types.KeyboardButton("сильный зуд и жжение в области влагалища")
        
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6) 

        bot.send_message(message.from_user.id, "какие симптомы вас беспокоят?", reply_markup=markup)
        bot.register_next_step_handler(message, female1)
    else:
        bot.register_next_step_handler(message, main_question)


def male1(message):
    global information
    if message.text in ["тошнота", "боль в суставах", "ноющие или схватывающие боли в зоне живота", "кровохарканье", "патологические выделения из уретры"]:
        information.append(message.text)

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("желтуха")
        item2=types.KeyboardButton("температура до 37.5")
        item3=types.KeyboardButton("изжога")
        item4=types.KeyboardButton("потемнение мочи")
        item5=types.KeyboardButton("увеличение местных лимфатических узлов")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)

        bot.send_message(message.from_user.id, "Какие ещё симптомы вас беспокоят?", reply_markup=markup)

        bot.register_next_step_handler(message, male2)


    else:
        bot.send_message(message.from_user.id, "вы ошиблись")
        bot.register_next_step_handler(message, fork)
    

def female1(message):
    global information
    if message.text in ["тошнота", "боль в суставах", "обесцвечивание кала", "ноющие или схватывающие боли в зоне живота", "кровохарканье", "Сильный зуд и жжение в области влагалища"]:
        information.append(message.text)


        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("задержка менструации")
        item2=types.KeyboardButton("температура до 37.5")
        item3=types.KeyboardButton("изжога")
        item4=types.KeyboardButton("потемнение мочи")
        item5=types.KeyboardButton("высыпания")
        item6=types.KeyboardButton("вязкие желтовато - белые выделения из влагалища с неприятным запахом")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)

        bot.send_message(message.from_user.id, "Какие ещё симптомы вас беспокоят?", reply_markup=markup)

        bot.register_next_step_handler(message, female2)

    else:
        bot.send_message(message.from_user.id, "вы ошиблись")
        bot.register_next_step_handler(message, fork)



def male2(message):
    global information
    if message.text in ["желтуха", "температура до 37.5", "изжога", "потемнение мочи", "увеличение местных лимфатических узлов"]:
        information.append(message.text)

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("был совершен незащищённый ПА")
        item2=types.KeyboardButton("контактировал с людьми болеющими туберкулёзом")
        item3=types.KeyboardButton("неожиданные боли в желудке")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)


        bot.send_message(message.from_user.id, "Почему вы решили обратиться?", reply_markup=markup)

        bot.register_next_step_handler(message, result)


    else:
        bot.send_message(message.from_user.id, "вы ошиблись")
        bot.register_next_step_handler(message, male1)


def female2(message):
    global information
    if message.text in ["задержка менструации", "температура до 37.5", "изжога", "потемнение мочи", "высыпания", "вязкие желтовато - белые выделения из влагалища с неприятным запахом"]:
        information.append(message.text)

        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("был совершен незащищённый ПА")
        item2=types.KeyboardButton("контактировал с людьми болеющими туберкулёзом")
        item3=types.KeyboardButton("неожиданные боли в желудке")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)


        bot.send_message(message.from_user.id, "Почему вы решили обратиться?", reply_markup=markup)

        bot.register_next_step_handler(message, result)


    else:
        bot.send_message(message.from_user.id, "вы ошиблись")
        bot.register_next_step_handler(message, female1)


def result(message):
    global information, repl_for_test
    if message.text in ["был совершен незащищённый ПА", "контактировал с людьми болеющими туберкулёзом", "неожиданные боли в желудке"]:
        information.append(message.text)

        message_for_user = result_func(information)

        bot.send_message(message.from_user.id, message_for_user, reply_markup=markup)

        bot.send_message(message.from_user.id, "https://matv864.github.io/progamist/images/for_project.jpg")

        information = []

    else:
        bot.send_message(message.from_user.id, "вы ошиблись")
        bot.register_next_step_handler(message, fork)


bot.polling()
