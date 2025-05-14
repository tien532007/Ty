import telebot

# Khởi tạo bot với token
TOKEN = '7526238474:AAEbWb2k7FgQ8expiOgguAHhu4eMXogGRYI'
bot = telebot.TeleBot(TOKEN)

# Xử lý lệnh /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Xin chào! Tôi là bot Telegram của bạn. Gõ /help để biết thêm.")

# Xử lý lệnh /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Danh sách lệnh:\n/start - Khởi động bot\n/help - Hiển thị trợ giúp")

# Xử lý tin nhắn văn bản bất kỳ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Bạn vừa nói: " + message.text)

# Chạy bot
bot.polling()
