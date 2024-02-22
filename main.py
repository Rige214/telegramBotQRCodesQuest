import html
import json
import configuration
import cv2
import telebot

bot = telebot = telebot.TeleBot(configuration.token)


@bot.message_handler(commands=['start'])
def message_start(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Приветствую, {html.escape(user_name)} !\n Бот создан для прохождения квеста'
                                      f' по QR-коду', parse_mode="HTML")

    try:
        with open("stepsQuests.json", "r") as fp:
            json.load(fp)
    except:
        print('file not found')
        bot.send_message(message.chat.id, 'Произошла ошибка. Пожалуйста, обратитесь к администратору')


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
    bot.send_message(message.chat.id, f'Содержимое QR-кода: {data}')

    with open("stepsQuests.json", "r") as fp:
        step_to_code = json.load(fp)
        code_to_step = {step: code for code, step in step_to_code.items()}
        if code_to_step.get(int(data)) == step_to_code:
            print('non json data')
            bot.send_message(message.chat.id, 'Пожалуйста, повторите попытку! ')
        else:
            bot.send_message(message.chat.id, code_to_step.get(int(data)))


bot.infinity_polling()
