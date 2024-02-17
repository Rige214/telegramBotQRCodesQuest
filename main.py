import json
import configuration
import cv2
import telebot

bot = telebot = telebot.TeleBot(configuration.token)


@bot.message_handler(commands=['start'])
def message_start(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Приветствую,<strong> {user_name} !</strong>\n Бот создан для прохождения квеста'
                                      f' по QR-коду', parse_mode="HTML")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    user_id = message.from_user.id
    file_telegram_id = message.photo[-1].file_id
    file_info = bot.get_file(file_telegram_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f"img/{user_id}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    img = cv2.imread(f"img/{user_id}.jpg")
    detector = cv2.QRCodeDetectorAruco()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    # bot.send_message(message.chat.id, f'Содержимое QR-кода: {data}')

    with open('stepsQuests.json', 'r') as j:
        json_data = json.load(j)
        if str(json_data['step_one']) == str(data):
            bot.send_message(message.chat.id, configuration.ACTION_ONE)
        elif str(json_data['step_two']) == str(data):
            bot.send_message(message.chat.id, configuration.ACTION_TWO)
        elif str(json_data['step_three']) == str(data):
            bot.send_message(message.chat.id, configuration.ACTION_THREE)
        elif str(json_data['step_four']) == str(data):
            bot.send_message(message.chat.id, configuration.ACTION_FOUR)
        else:
            print('no find json data')
            bot.send_message(message.chat.id, 'Пожалуйста, повторите попытку')


bot.infinity_polling()
