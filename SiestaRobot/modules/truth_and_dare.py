import html
import random
import SiestaRobot.modules.truth_and_dare_string as truth_and_dare_string
from SiestaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("ramdom1", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("ramdom2", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
