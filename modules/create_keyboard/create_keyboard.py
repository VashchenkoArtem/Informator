import aiogram
import modules.create_button.create_button as m_button

keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard=[[m_button.admin_button,m_button.client_button]])

keyboard_2 = aiogram.types.ReplyKeyboardMarkup(keyboard=[[m_button.registration_button,m_button.avtorisation_button]])

yes_or_not_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[m_button.agree_button,m_button.decline_button]])

create_keyboard= aiogram.types.ReplyKeyboardMarkup(keyboard=[[m_button.create_button]])

information_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[m_button.information_button],[m_button.pick_button,m_button.correct_button]])

