from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def answer(user_text):
    user_text = user_text.strip().lower()
    dictionary = {'hello':'Hello!', "bye":"Bye!"}
    usrmsg = dictionary.get(user_text, "I dont know!")
    return usrmsg

def start(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text = "Давай общаться!")

def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    user_text = update.message.text
    bot.sendMessage(update.message.chat_id, text = answer(user_text))

def run_bot():
    updater = Updater("287490937:AAFf7QZPLXcOGxIsfV-dEF-XqzAGEj5Tw5k")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()