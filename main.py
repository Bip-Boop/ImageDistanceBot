from image_math import ImageMath


from telegram.ext import *
import telegram

im = None
user_ids_even = dict()
def start_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Hello " + name)
    update.message.reply_text("Please share your image")

def image_handler(update, context):
    global user_ids_even
    global im
    uid = update.message.chat_id
    if uid in user_ids_even:
        user_ids_even[uid] = not user_ids_even[uid]
    else:
        user_ids_even[uid] = False
    
    file = update.message.photo[-1].get_file()
    path = file.download(f"output{uid}{int(user_ids_even[uid])}.jpg")

    if user_ids_even[uid] == False:
        update.message.reply_text("First image received. Need one more to compare")
    else:
        percentage = (im.calculate_conscious_distance(f"output{uid}0.jpg", f"output{uid}1.jpg")) * 100
        print(percentage, 100-percentage)
        update.message.reply_text(f"Similarity: {str(100.0- percentage)[:5]}%")
        distance = im.calculate_subconscious_distance(f"output{uid}0.jpg", f"output{uid}1.jpg")
        update.message.reply_text(f"Distance: {int(distance)} units")

    



def main():
    global im
    im = ImageMath()

    print("Started")
    TOKEN = ""
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))

    dp.add_handler(MessageHandler(Filters.photo, image_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()