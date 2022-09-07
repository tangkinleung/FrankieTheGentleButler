import random
import telebot
from telebot import custom_filters, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = telebot.TeleBot("5693289516:AAHpNSzWEz1vRsNBujSy4DjdGqRnme59060", parse_mode=None)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello {name}! I'm Frankie, the gentle butler. To start my services, please send 'You're hired!'.".format(name=message.from_user.first_name))
    

# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I help you?")

# Filter by text (Greetings)
@bot.message_handler(text=['hi Frankie', 'hello Frankie','hey Frankie', 'hola Frankie', 'oi Frankie', 'hiya Frankie', 'heya Frankie', 'howdy Frankie', 'greetings Frankie', 'sup Frankie', 'yo Frankie', 'whats up Frankie', 'whatsup Frankie', 'wassup Frankie', 'wass Frankie', 'Hi Frankie', 'Hello Frankie','Hey Frankie', 'Hola Frankie', 'Oi Frankie', 'Hiya Frankie', 'Heya Frankie', 'Howdy Frankie', 'Greetings Frankie', 'Sup Frankie', 'Yo Frankie', 'Whats up Frankie', 'Whatsup Frankie', 'Wassup Frankie', 'Wass Frankie', 'hi frankie', 'hello frankie','hey frankie', 'hola frankie', 'oi frankie', 'hiya frankie', 'heya frankie', 'howdy frankie', 'greetings frankie', 'sup frankie', 'yo frankie', 'whats up frankie', 'whatsup frankie', 'wassup frankie', 'wass frankie', 'Hi frankie', 'Hello frankie','Hey frankie', 'Hola frankie', 'Oi frankie', 'Hiya frankie', 'Heya frankie', 'Howdy frankie', 'Greetings frankie', 'Sup frankie', 'Yo frankie', 'Whats up frankie', 'Whatsup frankie', 'Wassup frankie', 'Wass frankie'])
def send_greetings(message):
    bot.reply_to(message, "Hola {name}!!".format(name=message.from_user.first_name))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    txt = message.text
    print(txt)
    if "You're hired!" in txt:
        bot.reply_to(message, "Yay I'm employed! What do you want me to do? Just send me a command!")
    
    
@bot.message_handler(commands=['eatwhat'])
def eatwhat(message):
    foodChoices = ["Collins🥩","Saizeriya🍝","Ma La dry🌶","Ma La Tang🍲","Takagi Ramen🍜","Pizza🍕","McDonald's🍔","Sushi🍣","Monster Curry🍛","Peneng Char Kway Teow🥢", "Soup Spoon🍲", "KFC🥠", "Burger King🍔", "Subway🥖", "Guzman Y Gomez🌮"]
    bot.reply_to(message, "I think you should eat ....." + random.choice(foodChoices))


# user state
state = {}

# # Markup
# markup = types.ReplyKeyboardMarkup()
# itembtna = types.KeyboardButton('Say you love me now!!!')
# itembtnb = types.KeyboardButton('What should I eat ah?')
# markup.row(itembtna)
# markup.row(itembtnb)
# def send_markup(cid):
#     bot.send_message(cid, "Choose an option:", reply_markup=markup)


# Register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())
bot.add_custom_filter(custom_filters.TextContainsFilter())

bot.infinity_polling()
