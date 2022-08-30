
import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Hello! Welcome To AreteBot :)')

def help_command(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About AreteBot Content
    /contact -> Information About Contact
                         
    """)

def content(update, context):
    update.message.reply_text("With this bot you can access many scientific articles. You can view articles on both scientific and philosophical topics.")

def contact(update, context):
    update.message.reply_text("You can contact the creator -> @the_sbh")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")
    
def main():
    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
main()
                   

