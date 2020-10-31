from telegram.ext import Updater
from telegram.ext import MessageHandler, CommandHandler, Filters

from modules import incoming_message_action, welcome, config, ls


if __name__ == '__main__':

    token = config["bot_token"]

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', welcome)
    dispatcher.add_handler(start_handler)

    ls_handler = CommandHandler('ls', ls)
    dispatcher.add_handler(ls_handler)

    incoming_message = MessageHandler(Filters.text, incoming_message_action)
    dispatcher.add_handler(incoming_message)

    updater.start_polling()


# TODO:
# - Do not download video if it's already available
# - Add systemd service
# - Replace system call with youtube-dl python package
# - Delete video function
