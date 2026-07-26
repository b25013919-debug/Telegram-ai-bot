import telebot
from google import genai

# Токен твоего бота из Telegram
TELEGRAM_TOKEN = "8994431659:AAGo93ht7rhVwzTfO75G2Rcro8Vgu4wIC70"
# Ключ от Google AI Studio (убедись, что внутри кавычек нет лишних пробелов)
GEMINI_API_KEY = "AQ.Ab8RN6IKuKkNBFnx9WFo6CUhBpfkPtsTvno89iiHdGQsXQlzfw"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
ai_client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой ИИ-бот. Напиши мне что-нибудь!")

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        response = ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=message.text,
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

print("ИИ-бот запущен...")
bot.infinity_polling()
