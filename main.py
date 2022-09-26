import random
import telebot
from telebot import custom_filters

bot = telebot.TeleBot("5693289516:AAHpNSzWEz1vRsNBujSy4DjdGqRnme59060", parse_mode=None)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello {name}! I'm Frankie, the gentle butler. Thanks for hiring me!".format(name=message.from_user.first_name))


# Handle '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How can I help you? *psst I actually cannot help you with anything*")

# Filter by text (Greetings)
@bot.message_handler(text=['hi Frankie', 'hello Frankie','hey Frankie', 'hola Frankie', 'oi Frankie', 'hiya Frankie', 'heya Frankie', 'howdy Frankie', 'greetings Frankie', 'sup Frankie', 'yo Frankie', 'whats up Frankie', 'whatsup Frankie', 'wassup Frankie', 'wass Frankie', 'Hi Frankie', 'Hello Frankie','Hey Frankie', 'Hola Frankie', 'Oi Frankie', 'Hiya Frankie', 'Heya Frankie', 'Howdy Frankie', 'Greetings Frankie', 'Sup Frankie', 'Yo Frankie', 'Whats up Frankie', 'Whatsup Frankie', 'Wassup Frankie', 'Wass Frankie', 'hi frankie', 'hello frankie','hey frankie', 'hola frankie', 'oi frankie', 'hiya frankie', 'heya frankie', 'howdy frankie', 'greetings frankie', 'sup frankie', 'yo frankie', 'whats up frankie', 'whatsup frankie', 'wassup frankie', 'wass frankie', 'Hi frankie', 'Hello frankie','Hey frankie', 'Hola frankie', 'Oi frankie', 'Hiya frankie', 'Heya frankie', 'Howdy frankie', 'Greetings frankie', 'Sup frankie', 'Yo frankie', 'Whats up frankie', 'Whatsup frankie', 'Wassup frankie', 'Wass frankie'])
def send_greetings(message):
    bot.reply_to(message, "Hola {name}!!".format(name=message.from_user.first_name))
    
# Eat where near WizVision command    
@bot.message_handler(commands=['eatwherenearwiz'])
def send_eatwherenearwiz(message):
    bot.reply_to(message, "I think you should eat at... {food} today".format(food = random.choice(foodChoicesWizWhere)))

# Eat what near WizVision command
@bot.message_handler(commands=['eatwhatnearwiz'])
def send_eatwhatnearwiz(message):
    #bot.reply_to(message, "I think you should eat..." +random.choice(foodChoicesWiz)+ " today. " +random.choice(honestyChoices))
    bot.reply_to(message, "I think you should eat..." +random.choice(foodChoicesWiz)+ " today.")

# Eat what command
@bot.message_handler(commands=['eatwhat'])
def send_eatwhat(message):
    bot.reply_to(message, "I think you should eat... {food} today".format(food = random.choice(foodChoices)))

# Song recommendation command
@bot.message_handler(commands=['song'])
def send_song(message):
    bot.reply_to(message, "I think you should listen to... {song} today".format(song = random.choice(songChoices)))

# Lists of food and places (Static)
foodChoices = ["Collins🥩","Saizeriya🍝","Ma La dry🌶","Ma La Tang🍲","Takagi Ramen🍜","Pizza🍕","McDonald's🍔","Sushi🍣","Monster Curry🍛","Peneng Char Kway Teow🥢", "Soup Spoon🍲", "KFC🥠", "Jollibee🥠", "Burger King🍔", "Subway🥖", "Guzman Y Gomez🌮"]
foodChoicesWizWhere = ["downstairs bus stop there", "Circuit road there", "Paya Lebar there", "downstairs basement there", "downstairs expensive there"]
foodChoicesWiz = ["Chicken Rice🐔🍚", "Nasi Lemak🥥🍚", "Cai Png🥬🍚", "sum noodles🍜", "Japaneses🎎"]
honestyChoices = ["", "But if you ask me, I think you should just eat somewhere else for more variety of food..."]
songChoices = [
    "Clinton Kane - CHICKEN TENDIES (https://music.youtube.com/watch?v=QvVW-ZmuSXg)", 
    "Clinton Kane - I GUESS I'M IN LOVE (https://music.youtube.com/watch?v=5LMqtzgXaRQ)", 
    "Hayd - Head In The Clouds (https://music.youtube.com/watch?v=UlL4NidGa4c)",
    "Justin Bieber - Intentions (https://music.youtube.com/watch?v=RcSX0hOWcQ0)",
    "WiFi歪歪 - 就忘了吧 (https://music.youtube.com/watch?v=G21CwEVL17Y)"
    ]


# Register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())
bot.add_custom_filter(custom_filters.TextContainsFilter())

bot.infinity_polling()
