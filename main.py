from image_math import ImageMath


from telegram.ext import *
import telegram

user_ids_even = dict()
def start_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Hello " + name)
    update.message.reply_text("Please share your image")

def image_handler(update, context):
    global user_ids_even
    if update.message.chat_id in user_ids_even:
        user_ids_even[update.message.chat_id] = not user_ids_even[update.message.chat_id]
    else:
        user_ids_even[update.message.chat_id] = False
    
    file = update.message.photo[-1].get_file()
    path = file.download(f"output{update.message.chat_id}{int(user_ids_even[update.message.chat_id])}.jpg")
    update.message.reply_text("Image received")
    update.message.reply_text("Hello " + str(update.message.chat_id))

def main():
    print("Started")
    TOKEN = "token"
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(MessageHandler(Filters.photo, image_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()