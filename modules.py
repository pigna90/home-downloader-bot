import re
import logging
import subprocess
import json
from os import listdir
from os.path import isfile, join

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

with open('config.json') as f:
    config = json.load(f)


def welcome(update, context):
    if update.message.chat.username not in config["valid_users"]:
        return False

    logging.info(f"[System Log] Chat initiated by user {update.message.chat.username}")
    context.bot.send_message(chat_id=config["owner_chat_id"], text=f"Chat initiated by user {update.message.chat.username}")
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome!")


def download_video(url):
    logging.info(f"Downloading video from {url}")
    bash_command = f'youtube-dl -f bestvideo+bestaudio {url} -o {config["out_dir"]}%(title)s.%(ext)s'

    process = subprocess.run(bash_command.split(), stdout=subprocess.PIPE)
    out = process.stdout.decode("utf-8")

    if "Merging formats into" not in out and "[download]" not in out:
        return False
    else:
        return True


def incoming_message_action(update, context):
    if update.message.chat.username not in config["valid_users"]:
        return False

    logging.info(f"Message received: {update.message.chat.username} - [{update.message.text}]")

    # Parse URL if necessary
    try:
        url = re.search("(?P<url>https?://[^\s]+)", update.message.text).group("url")
    except (TypeError, AttributeError):
        url = None

    # Check URL integrity
    if url and any(x == url for x in config["valid_websites"]):
        context.bot.send_message(chat_id=update.message.chat_id, text="Downloading :)")
        out = download_video(url)
        if out:
            context.bot.send_message(chat_id=update.message.chat_id, text="Download completed!")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Download NOT possible!")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Link not valid :(")


def ls(update, context):
    if update.message.chat.username not in config["valid_users"]:
        return False

    logging.info("Call /ls command.")

    fnames_video = [f for f in listdir(config["out_dir"]) if isfile(join(config["out_dir"], f))]
    context.bot.send_message(chat_id=update.message.chat_id, text="\n".join(fnames_video))