# Консольные логи
import logging

# Библиотеки для работы с API Telegram
from telegram import (
        Update,
        InlineKeyboardButton,
        InlineKeyboardMarkup,
        )

from telegram.ext import (
        Application,
        ContextTypes,
        CommandHandler,
        CallbackQueryHandler,
        )

# Консольные логи
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton('Русский Язык', callback_data="rus"),
            InlineKeyboardButton('Математика', callback_data="mat")
        ],
        [
            InlineKeyboardButton('Обществознание', callback_data="soc"),
            InlineKeyboardButton('Информатика', callback_data="inf")
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
            "Выберете предмет:",
            reply_markup=reply_markup
            )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
            f"Выбранный предмет: {query.data}"
            )


def main() -> None:
    app = Application.builder().token(
            'TOKEN'
            ).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()


if __name__ == '__main__':
    main()
