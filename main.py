from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, RegexHandler
import config, reply

def main():
    updater = Updater(token=config.TOKEN)

    conversation = ConversationHandler(
        entry_points = [
            CommandHandler('start', reply.start),
            MessageHandler(Filters.all, reply.error_start),
        ],

        states = {
            BASE: [

            ]
        }
    )