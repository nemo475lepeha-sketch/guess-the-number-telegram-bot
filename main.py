'''Main bot entry point.'''

from cfg.config import bot, data
from handlers import messages
from handlers.callbacks import callbacks


# Start command handler: initialize the game session and show the main menu.
@bot.message_handler(commands=['start'])
def start_game(message):
    '''Handle the /start command.'''
    messages.start_game(message, bot)


# Callback handler: process inline keyboard actions.
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    '''Handle callback queries from inline buttons.'''
    handler = callbacks.get(call.data)
    if handler: handler(call, bot)
    else: bot.answer_callback_query(call.id, 'Неизвестная команда')


# Text handler: only handle numeric guesses if the user is in an active game.
@bot.message_handler(content_types=['text'])
def text_handler(message):
    '''Handle text messages from the user during the game.'''
    if data[message.from_user.id]['attempts'] > 0: messages.game_logic(message, bot)
    else: bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


# Delete unsupported media and sticker messages to keep the chat clean.
@bot.message_handler(content_types=['sticker', 'photo', 'video', 'document', 'audio', 'voice', 'animation'])
def media_handler(message):
    '''Delete unsupported media and sticker messages.'''
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


print(f'bot is running...\npress Ctrl+C to stop the bot')
bot.polling(none_stop=True)