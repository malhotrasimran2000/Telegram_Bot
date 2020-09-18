
import logging  
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update,ReplyKeyboardMarkup
from utils import get_reply
from utils import fetch_news,topics_keyboard



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

def news(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="Choose a category",
        reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard,one_time_keyboard=True))

def reply_text(bot,update):
   
    intent,reply=get_reply(update.message.text,update.message.chat_id)
  
    if intent=="get_news":
        reply_text="Okay!Here's the news"
        articles=fetch_news(reply)
        for article in articles:
            update.message.reply_text(article['link'])

    else:
        update.message.reply_text(reply)


def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update,update.error)


bot=Bot(TOKEN)
try:
    bot.set_webhook("https://radiant-headland-89852.herokuapp.com/"+TOKEN)

except Exception as e:
    print(e)
    
dp=Dispatcher(bot,None)

dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('help',_help))
dp.add_handler(CommandHandler('news',news))
dp.add_handler(MessageHandler(Filters.text,reply_text))
dp.add_error_handler(error)



if __name__ == '__main__':
    app.run(port=8443)
