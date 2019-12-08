from telegram.ext import Updater
from config import MODE, TOKEN, PORT
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

if MODE == "develop":

    def run(updater):
        updater.start_polling()


elif MODE == "production":

    def run(updater):
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(f"https://ifixitbot.herokuapp.com/{TOKEN}")


else:
    logger.error("You need to specify a working MODE")


def main():
    updater = Updater(TOKEN, use_context=True)

    # Dispatcher for handlers
    dp = updater.dispatcher

    run(updater)

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
