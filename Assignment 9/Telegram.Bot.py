import telebot
import random
import khayyam
import qrcode
from gtts import gTTS

bot = telebot.TeleBot("6445991863:AAECQLOW52eNhC1KXF7d_fF2n4B7cy0mgjg", parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    welcome_message = f"خوش اومدی به بات (( {name} )) 😍"
    bot.reply_to(message, welcome_message)


@bot.message_handler(commands= ['game'])
def game(message):
    global bot_state
    global computer_num
    markup = telebot.types.ReplyKeyboardMarkup(row_width= 1)
    # button = telebot.types.KeyboardButton("/new_game")
    # markup.add(button)
    computer_num = random.randint(0,100)
    bot.send_message(message.chat.id, " 🤔 یه عدد بین 0 تا 100 بگو " , reply_markup=markup)
    

    @bot.message_handler(func= lambda m:True)
    def guess_game(message):
        global computer_num

        if int(message.text) < computer_num:
            bot.send_message(message.chat.id, "👆🏻 برو بالاتر ", reply_markup=markup )
            
        elif int(message.text) > computer_num:
            bot.send_message(message.chat.id, "👇🏻 بیا پایین تر", reply_markup= markup ) 
            
        elif int(message.text) == computer_num:
            bot.send_message(message.chat.id, " 🥳😍 افرین درست حدس زدی", reply_markup= telebot.types.ReplyKeyboardRemove(selective=True))


@bot.message_handler(commands= ['age'])
def age(message):
    global bot_state
    age_of_user = bot.send_message(message.chat.id, "تاریخ تولد میلادی ات رو به این صورت وارد کن : (year/month/day)")
    bot.register_next_step_handler(age_of_user , age_calculator)

def age_calculator(message):
        birthday = (str(message.text)).split("/")

        age_differnce = khayyam.JalaliDatetime.now()- khayyam.JalaliDatetime(birthday[0], birthday[1], birthday[2])

        year = age_differnce.days // 365
        age_differnce = age_differnce.days % 365
        month = age_differnce // 30
        day = (age_differnce % 30) -7

        bot.send_message(message.chat.id, "سن شما : "+ str(year) + " سال و "+ str(month) + " ماه و "+ str(day) + " روز.")


@bot.message_handler(commands= ['voice'])
def voice(message):
    global bot_state
    user_text = bot.send_message(message.chat.id, "🧐 یه متن انگلیسی تایپ کن برام ")
    bot.register_next_step_handler(user_text, create_voice)

def create_voice(message):
    audio = gTTS(text = message.text, lang = "en", slow = False)
    audio.save("audio.mp3")
    audio_file = open("audio.mp3", "rb")
    bot.send_voice(message.chat.id, audio_file)


@bot.message_handler(commands= ['max'])
def max(message):
    global bot_state
    user_nums = bot.send_message(message.chat.id, "لیستی از اعداد انگلیسی رو وارد کن،مثلا => 12,13,14,15  ")
    bot.register_next_step_handler(user_nums, find_max_num)

def find_max_num(message):
    numbers = message.text.split(",")
    max_num = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > max_num:
            max_num = int(numbers[i])
    bot.send_message(message.chat.id, str(max_num) + " 👉🏻 بزرگ ترین عدد")


@bot.message_handler(commands= ['argmax'])
def argmax(message):
    global bot_state
    user_nums = bot.send_message(message.chat.id, "لیستی از اعداد انگلیسی رو وارد کن،مثلا => 12,13,14,15  ")
    bot.register_next_step_handler(user_nums, find_index)

def find_index(message):
    numbers = message.text.split(",")
    max = 0
    index = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > max:
            max = int(numbers[i])
            index = i + 1
    bot.send_message(message.chat.id, "اندیس عدد " + str(max) + " در خانه شماره  " + str(index) + " است")


@bot.message_handler(commands= ['qrcode'])
def QR_code(message):
    global bot_state
    user_text = bot.send_message(message.chat.id, "متن انگلیسی بده QRcode تحویل بگیر")
    bot.register_next_step_handler(user_text, Create_QRcode)

def Create_QRcode(message):
    user_qrcode = qrcode.make(message.text)
    user_qrcode.save("QRcode.jpg")
    QRcode = open("QRcode.jpg", "rb")
    bot.send_photo(message.chat.id, QRcode)


@bot.message_handler(commands= ["help"])
def help(message):
    global bot_state
    bot.reply_to(message, """ 
    /start : خوش اومدی . . . \n
    /game : بازی حدس اعداد \n
    /age  : تبدیل تاریخ تولد میلادی به سن \n
    /voice : تبدیل متن انگلیسی به ویس \n
    /max : دریافت لیستی از اعداد انگلیسی و پیدا کردن بزرگ ترین مقدار \n
    /argmax : دریافت لیستی از اعداد انگلیسی و پیدا کردن اندیس بزرگترین مقدار \n
    /qrcode : QRcode دریافت متن انگلیسی و تبدیل ان به \n
    /help : نمایش منوی بات \n
    """)


bot.infinity_polling()