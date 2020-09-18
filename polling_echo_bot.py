#Polling Program
#(Resource intensive)



import logging 
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import Update

logging.basicConfig(format='%(asctime)s - %(name)s- %(levelname)s-%(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN="1272801736:AAHN2rMaLsSPqXjv8hYaSWYbrjJUXoqVySo"




def start(update,context):
    print(update)
    author=update.message.from_user.first_name
    reply="Hi! {}".format(author)
    update.message.reply_text(reply)
    

def _help(update,context):
    help_txt="What help do you want?"
    update.message.reply_text(help_txt)

def echo_text(update,context):
    reply=update.message.text
    update.message.reply_text(reply)

'''
def echo_sticker(update,context):
     update.sendSticker(chat_id=update.message.chat_id,sticker=update.message.file_id)
'''

def error(update,context):
    logger.error("Update '%s' caused error '%s'",update,context.error)




def main():
    updater=Updater(TOKEN,use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    #dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    

    updater.start_polling() #Triggers the polling process :keeps sending requests to the Telegram Server
    logger.info("Started polling...")
    updater.idle() #Waits for Ctrl +C



if __name__ == '__main__':
    main()
