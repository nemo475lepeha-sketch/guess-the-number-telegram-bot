import random

from cfg import keyboards as kb
from cfg.config import data

# Main menu callback: reset user state and show the opening screen.
def main_menu(call, bot):
    '''bot edit message to show main menu'''
    data[call.from_user.id] = {'attempts': -1, 'message_id': call.message.id}
    bot.edit_message_text(
        text='Привет, это игра в угадай цифру! Нажми "Играть" если готов',
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        reply_markup=kb.main_keyboard(),
    )


# Rules callback: show the game instructions without changing the game state.
def show_rules(call, bot):
    '''bot edit message to show game rules'''
    data[call.from_user.id] = {'attempts': -1, 'message_id': call.message.id}
    bot.edit_message_text(
        text=(
            'Правила: я загадываю число, а ты пишешь свои предположения.\n'
            'Я буду говорить, больше или меньше твоё число.\n'
            'Твоя задача угадать число за ограниченное количество попыток.'
        ),
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        reply_markup=kb.back_menu(),
    )


# Difficulty selection callback: show the mode choice menu.
def play_game(call, bot):
    '''bot edit message to show game difficulty options'''
    data[call.from_user.id] = {'attempts': -1, 'message_id': call.message.id}
    bot.edit_message_text(
        text='Выбери сложность:\nЛегкая - 15 попыток\nСредняя - 10 попыток\nСложная - 5 попыток',
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        reply_markup=kb.play_keyboard(),
    )


# Game mode callbacks: initialize a hidden number and attempt counter for the user.
def easy_level(call, bot):
    '''bot edit message to start easy game mode'''
    data[call.from_user.id] = {
        'attempts': 15,
        'number': random.randint(1, 100),
        'message_id': call.message.id,
    }
    bot.edit_message_text(
        text='Я загадываю число от 1 до 100... Ваши предположения?\n(У вас 15 попыток - напишите число)',
        chat_id=call.message.chat.id,
        message_id=call.message.id,
    )


def medium_level(call, bot):
    '''bot edit message to start medium game mode'''
    data[call.from_user.id] = {
        'attempts': 10,
        'number': random.randint(1, 100),
        'message_id': call.message.id,
    }
    bot.edit_message_text(
        text='Я загадываю число от 1 до 100... Ваши предположения?\n(У вас 10 попыток - напишите число)',
        chat_id=call.message.chat.id,
        message_id=call.message.id,
    )


def hard_level(call, bot):
    '''bot edit message to start hard game mode'''
    data[call.from_user.id] = {
        'attempts': 5,
        'number': random.randint(1, 100),
        'message_id': call.message.id,
    }
    bot.edit_message_text(
        text='Я загадываю число от 1 до 100... Ваши предположения?\n(У вас 5 попыток - напишите число)',
        chat_id=call.message.chat.id,
        message_id=call.message.id,
    )


# Callback registry for all menu and game actions.
callbacks = {
    'menu': main_menu,
    'rules': show_rules,
    'play': play_game,
    'easy': easy_level,
    'medium': medium_level,
    'hard': hard_level,
}
