#Webhook Server Program 
#Before starting a program,we tell the Telegram server that we have
# a callback URL(Url on which my server will be running and it will keep accepting any requests from the server)
#If any request from any telegram user is received by the server,it sends it to the callback URL
#Telegram Server is responsible for triggering if there is any request

#Setting up a Server


import logging  
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update

#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s- %(levelname)s-%(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN="1272801736:AAHN2rMaLsSPqXjv8hYaSWYbrjJUXoqVySo"

app=Flask(__name__)   #creating a Flask app object

@app.route('/')
def index():
	return "Hello!"


@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
	"""webhook view which receives updates from telegram"""

	#create update object from json-format request data
	update=Update.de_json(request.get_json(),bot)
	#process update
	dp.process_update(update) #dispatcher responsible for handling updates
	return "ok"





def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply="Hi! {}".format(author)
    update.message.reply_text(reply)
    

def _help(bot,update):
    help_txt="What help do you want?"
    update.message.reply_text(help_txt)

def echo_text(bot,update):
    reply=update.message.text
    update.message.reply_text(reply)

"""
def echo_sticker(bot,update):
     bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
"""

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update,update.error)



if __name__ == '__main__':
    bot=Bot(TOKEN)
    bot.set_webhook("https://84ab4048ba79.ngrok.io/"+TOKEN)
    dp=Dispatcher(bot,None)

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    #dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)

    app.run(port=8443)
