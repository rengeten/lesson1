from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem, answer, solver, str_clac, full_moon

def start(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, text = "Давай общаться!")

def count(bot, update):
    print(update.message.text)
    msg = update.message.text
    msg = msg.split(' ')
    print(len(msg))
    output = len(msg) - 1
    full_output = 'Предложение содержит {} слов'.format(output)
    bot.sendMessage(update.message.chat_id, text = full_output)

def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    user_text = update.message.text
    user_text = user_text.strip().lower()
    if "=" in user_text:
        bot.sendMessage(update.message.chat_id, text = solver.solver(user_text))
    elif "сколько будет" in user_text:
        bot.sendMessage(update.message.chat_id, text = str_clac.str_clac(user_text))
    elif "когда ближайшее полнолуние" in user_text:
        bot.sendMessage(update.message.chat_id, text = full_moon.full_moon(user_text))
    else:    
        bot.sendMessage(update.message.chat_id, text = answer.answer(user_text))

def run_bot():
    updater = Updater("287490937:AAFf7QZPLXcOGxIsfV-dEF-XqzAGEj5Tw5k")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("count", count))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    run_bot()