import aiogram

admin_button = aiogram.types.KeyboardButton(text='Адміністратор')
client_button = aiogram.types.KeyboardButton(text='Кліент')

registration_button = aiogram.types.KeyboardButton(text='Реєстрація')
avtorisation_button = aiogram.types.KeyboardButton(text='Авторизація')

agree_button = aiogram.types.InlineKeyboardButton(text='Згоден', callback_data= 'Згоден')
decline_button = aiogram.types.InlineKeyboardButton(text='Не згоден',  callback_data= 'Не згоден')

create_button = aiogram.types.KeyboardButton(text='Створити сповіщення')

pick_button = aiogram.types.InlineKeyboardButton(text = "Обрати",callback_data = "Обрати")
information_button = aiogram.types.InlineKeyboardButton(text="Інформація", callback_data= "Інформація")
correct_button = aiogram.types.InlineKeyboardButton(text="Підтвердити", callback_data= "Підтвердити")
