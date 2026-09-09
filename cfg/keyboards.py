from telebot import types

def main_keyboard():
    '''returns the main menu keyboard'''
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Играть', callback_data='play')
    btn2 = types.InlineKeyboardButton('Правила', callback_data='rules')

    markup.row(btn1, btn2)
    return markup

def back_menu():
    '''returns the back button for the main menu'''
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='menu')

    markup.row(btn1)
    return markup

def play_keyboard():
    '''returns the game mode selection keyboard'''
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Легко', callback_data='easy')
    btn2 = types.InlineKeyboardButton('Средне', callback_data='medium')
    btn3 = types.InlineKeyboardButton('Сложно', callback_data='hard')
    btn4 = types.InlineKeyboardButton('Назад', callback_data='menu')

    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    return markup

