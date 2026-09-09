from cfg import keyboards as kb
from cfg.config import data

# Start command: reset session data and send the main menu.
def start_game(message, bot):
    '''start message, initialize user data and send main menu'''
    data[message.from_user.id] = {
        'attempts': -1,
        'message_id': message.message_id,
    }
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет, это игра в угадай цифру! Нажми "Играть" если готов',
        reply_markup=kb.main_keyboard(),
    )


# Main game logic: validate input, update attempts, and respond to guesses.
def game_logic(message, bot):
    '''game logic, check user input and respond accordingly'''
    user_id = message.from_user.id

    if user_id not in data:
        return

    state = data[user_id]
    if message.content_type != 'text':
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    text = (message.text or '').strip()
    if not text.isdigit():
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    elif not (1 <= int(text) <= 100):
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    attempts = state.get('attempts', -1)
    if attempts <= 0:
        if attempts == 0 and state.get('number') is not None:
            bot.edit_message_text(
                text=(
                    f'Ты проиграл, у тебя кончились попытки! Я загадал число: {state["number"]}.\n'
                    'Нажми "Играть" чтобы начать заново.'
                ),
                chat_id=message.chat.id,
                message_id=state.get('message_id', message.message_id),
            )
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    guess = int(text)
    number = state['number']
    state['attempts'] -= 1
    remaining_attempts = state['attempts']
    message_id = state.get('message_id', message.message_id)

    if guess == number:
        state['attempts'] = -1
        bot.edit_message_text(
            text=(
                f'Ура, ты угадал! Это число: {number}.\n'
                'Нажми "Играть", чтобы сыграть ещё раз.'
            ),
            chat_id=message.chat.id,
            message_id=message_id,
        )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    if remaining_attempts <= 0:
        bot.edit_message_text(
            text=(
                f'Не угадал. Я загадал число: {number}.\n'
                'Нажми "Играть", чтобы начать заново.'
            ),
            chat_id=message.chat.id,
            message_id=message_id,
            reply_markup=kb.main_keyboard(),
        )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        return

    if guess < number:
        bot.edit_message_text(
            text=(
                f'Не угадал, мое число больше твоего предположения! ({guess})\n'
                f'У тебя осталось {remaining_attempts} попыток.'
            ),
            chat_id=message.chat.id,
            message_id=message_id,
        )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        bot.edit_message_text(
            text=(
                f'Не угадал, мое число меньше твоего предположения! ({guess})\n'
                f'У тебя осталось {remaining_attempts} попыток.'
            ),
            chat_id=message.chat.id,
            message_id=message_id,
        )
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

