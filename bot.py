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


lessions = {'rus': 'Русский Язык',
            'mat': 'Математика',
            'soc': 'Обществознание',
            'inf': 'Информатика'}


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
        [
            InlineKeyboardButton('Выход', callback_data='exit')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
            "Выберете предмет:",
            reply_markup=reply_markup
            )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data != 'exit':
        lession = lessions[query.data]
        reply_markup = reply_markup_get(query.data)
        await query.edit_message_text(
            f"Выбранный предмет: {lession}",
            reply_markup=reply_markup
        )
    else:
        await update.message.text(text='Пока🖐️')


def reply_markup_get(id):
    if id == 'rus':
        keybord = [
                [
                    InlineKeyboardButton('Задание 9', callback_data='rus-9'),
                ],
                [
                    InlineKeyboardButton('Выход', callback_data='exit')
                ]
        ]
    elif id == 'mat':
        keybord = [
                [
                    InlineKeyboardButton('Выход', callback_data='exit')
                ]
        ]
    elif id == 'soc':
        keybord = [
                [
                    InlineKeyboardButton('Выход', callback_data='exit')
                ]
        ]
    elif id == 'inf':
        keybord = [
                [
                    InlineKeyboardButton('Выход', callback_data='exit')
                ]
        ]
    return InlineKeyboardMarkup(keybord)


def main() -> None:
    app = Application.builder().token(
            'TOKEN'
            ).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()


if __name__ == '__main__':
    main()
