import aiogram
import aiogram.filters
import asyncio
import modules.bot_create.bot_create as m_bot
import modules.create_dispatcher.create_dispatcher as m_dispatcher
import modules.create_keyboard.create_keyboard as m_keyboard
import modules.sql3.sql3 as m_sql3
import requests
caption = None
@m_dispatcher.dp.message(aiogram.filters.CommandStart())
async def start(message: aiogram.types.Message):
    await message.answer(text= 'Вітаємо!',reply_markup= m_keyboard.keyboard)
    
@m_dispatcher.dp.message(lambda message: message.text == 'Адміністратор')
async def admin(message: aiogram.types.Message):
    await message.answer(text='Добре. Оберіть один з варіантів', reply_markup= m_keyboard.keyboard_2)

@m_dispatcher.dp.message(lambda message: message.text == 'Реєстрація')
async def registration(message: aiogram.types.Message):
    await message.answer(text='Для реєстрації введіть дані у форматі :\n Email, Nickname, Password, Phone Number')
message_id = None
message_chat = None
email1 = None
nickname1 = None
password1= None
phone_number1 = None

@m_dispatcher.dp.message() 
async def reg_2(message: aiogram.types.Message):
    if message.text == "Створити сповіщення":
        await message.answer(text = "Добре! Для того щоб відправляти сповіщення вам потрібно написати: \nUrl \nОпис картинки")
    if len(message.text.split("\n")) == 2:
        global message_id, message_chat, email1, nickname1, password1, phone_number1,caption, message_1
        url,caption1 = map(str.strip,message.text.split("\n"))
        url_response = requests.get(url)
        caption = caption1
        with open("image.jpg","wb") as file:
            file.write(url_response.content)
            await m_bot.bot.send_photo(message.chat.id,url,reply_markup = m_keyboard.information_keyboard)
            return caption
    try:
        email, nickname, password, phone_number = map(str.strip, message.text.split(','))   
        message_1 = message
        message_id = message.chat.id
        message_chat = message
        email1 = email
        nickname1 = nickname
        password1 = password
        phone_number1 = phone_number
        await m_bot.bot.send_message(chat_id= -1002102359292, text= f'{email}\n{nickname}\n{password}\n{phone_number}\n Прийняти до адміністраторів чи ні?',
                                    reply_markup = m_keyboard.yes_or_not_keyboard)
        await message.answer(text='Реєстрація пройшла успішно! Очікуйте підтвердження від модератора.')
        return message_id, message_chat, email1, nickname1, password1, phone_number1, message_1
    except:
        pass
message_1 = None
@m_dispatcher.dp.callback_query()
async def callback_query(callback: aiogram.types.CallbackQuery):
    global message_id, message_1,  email1, nickname1, password1, phone_number1, caption, message_chat
    count = 0 
    if "Згоден" in callback.data and count == 0 :
        await m_bot.bot.send_message(text = "Вас прийняли!",chat_id = message_id)
        count += 1
        m_sql3.cursor.execute('''INSERT INTO admins (
                   user_id, email, nickname, password, phone_number)
                   VALUES (?,?,?,?,?)''', (message_chat.from_user.id, email1, nickname1, password1, phone_number1))
        m_sql3.tabel.commit() 
        await message_chat.answer(text = "Тепер ви можете створювати сповіщення", reply_markup = m_keyboard.create_keyboard)
    if "Не згоден" in callback.data and count == 0:
        await m_bot.bot.send_message(text = "Нажаль, вас не прийняли",chat_id = message_id)
        count +=1 
    if "Інформація" in callback.data:
        await message_chat.answer(text=f"Подробиці до товару:\n{caption}")
# count= 0
# @m_dispatcher.dp.message(aiogram.filters.CommandStart())
# async def bot_start(message: aiogram.types.Message):
#     await message.answer(text='Вітаємо', 
#                          reply_markup= m_keyboard.keyboard)
    
# @m_dispatcher.dp.message()
# async def update_keyboard(message: aiogram.types.Message):
#     global count
#     if message.text == 'Адміністратор':
#         await message.answer(text='Будь-ласка оберіть один з варіантів',
#                              reply_markup=m_keyboard.keyboard_2)
#     if message.text =='Реєстрація':
#         await message.answer(text= 'Пройдіть реєстрацію. Запишіть дані в такому вигляді: \nEmail \nNickname \nPassword \nPhone ')
#         # if message.text != "Реєстрація":
#         message_text = f"{message.from_user.first_name} хоче приєднатися до адміністраторів. Ви згодні чи ні?"
#         chat_id = -1002102359292
#         await m_bot.bot.send_message(chat_id = chat_id, text=message_text, reply_markup=m_keyboard.yes_or_not_keyboard)




# @m_dispatcher.dp.callback_query()
# async def yes_or_no(callback: aiogram.types.CallbackQuery):
#     global count
#     if callback.data == 'Згоден':
#         count =1
#         # print(count)
#         return count

# @m_dispatcher.dp.message()
# async def discription(message: aiogram.types.Message):
#     global count
#     print(count)
#     if count == 1:
#         await message.answer(text='Hi')
#         print(count)