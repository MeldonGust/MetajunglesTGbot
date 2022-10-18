# Импорты
import logging


from aiogram.utils.deep_linking import decode_payload
from aiogram import Bot, Dispatcher, executor, types, utils

from models import *

# Переменные
API_TOKEN = '5352033299:AAFwC-aKX5oHmeQtQpusIoeryie5ILB5-Rk' 
ref_link = 'https://telegram.me/{}?start={}'
channel_link = 'https://t.me/metajungles_ru'

# Настройка
logging.basicConfig(level=logging.INFO)

# Иницилизация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Базовые функции



# Хэндлер старта
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

  # Проверка базы данных
  cur = connection.cursor()
  cur.execute("""SELECT user_id FROM users""")
  users_id = cur.fetchall() # айди всех участников с табилцы
  user_id = message.from_user.id # айди зареганного участника  
  # проверяем, есть ли новый пользователь в базе данных
  if str(user_id) in str(users_id):
    
    #батоны. вкусные.
    refferals_btn = types.KeyboardButton('Рефералы и ссылка👥')
    buy_btn = types.KeyboardButton('Купить📈')
    chat_btn = types.KeyboardButton('Вступить в чат💬')
    check_table_btn = types.KeyboardButton('Посмотреть участников👤')
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(refferals_btn, buy_btn, chat_btn, check_table_btn)
    
    await bot.send_message(message.chat.id, text = 'Ваш айди уже есть в базе данных.', reply_markup =  markup)
    
  else:
    # Реферальная система
    start_command = message.text
    refferer_id = str(start_command[7:])
    if str(refferer_id) != "":
      if str(refferer_id) != str(message.from_user.id):
        
        add_user(message.from_user.id, refferer_id)
        refferals_btn = types.KeyboardButton('Рефералы и ссылка👥')
        buy_btn = types.KeyboardButton('Купить📈')
        chat_btn = types.KeyboardButton('Вступить в чат💬')
        check_table_btn = types.KeyboardButton('Посмотреть участников👤')
    
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(refferals_btn, buy_btn, chat_btn, check_table_btn)
        
        await bot.send_message(message.from_user.id, text = 'Это официальный бот NFT коллекции METAJUGNLES. Здесь вы сможете пользоваться реферальной программой, участвовать в розыгрышах и эирдропах.', reply_markup = markup)

      else:
        
        refferals_btn = types.KeyboardButton('Рефералы и ссылка👥')
        buy_btn = types.KeyboardButton('Купить📈')
        chat_btn = types.KeyboardButton('Вступить в чат💬')
        check_table_btn = types.KeyboardButton('Посмотреть участников👤')
    
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(refferals_btn, buy_btn, chat_btn, check_table_btn)
        
        await bot.send_message(message.from_user.id, text = 'По собственной ссылке регистрироваться нельзя!')
        add_user(message.from_user.id, 0)
        
    else:
      
      refferals_btn = types.KeyboardButton('Рефералы и ссылка👥')
      buy_btn = types.KeyboardButton('Купить📈')
      chat_btn = types.KeyboardButton('Вступить в чат💬')
      check_table_btn = types.KeyboardButton('Посмотреть участников👤')
    
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      markup.add(refferals_btn, buy_btn, chat_btn, check_table_btn)
      
      await bot.send_message(message.from_user.id, text = 'Это официальный бот NFT коллекции METAJUGNLES.\nЗдесь вы сможете пользоваться реферальной программой, участвовать в розыгрышах и эирдропах.', reply_markup = markup)
      
      add_user(message.from_user.id, 0)  
      connection.commit()
    
    refferals_btn = types.KeyboardButton('Рефералы и ссылка👥')
    buy_btn = types.KeyboardButton('Купить📈')
    chat_btn = types.KeyboardButton('Вступить в чат💬')
    check_table_btn = types.KeyboardButton('Посмотреть участников👤')
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(refferals_btn, buy_btn, chat_btn, check_table_btn)
  

# Хэндлер для рега пользователя
@dp.message_handler()
async def func(message: types.Message):
  
  user_channel_status = await bot.get_chat_member(chat_id='-1001235244140', user_id = message.from_user.id)

  if user_channel_status["status"] != 'left':
    if message.text == 'Купить📈':
      if ref_id_count(message.from_user.id) != 0:
        if check_ref_per(message.from_user.id) == 0:
          refs_increase(ref_id_count(message.from_user.id))
          ref_per_increase(message.from_user.id)
          await bot.send_message(ref_id_count(message.from_user.id), 'По вашей ссылке зарегистрировался пользователь!')
          
      await bot.send_message(message.from_user.id, text = 'Как предзаказать НФТ?\n'
'\n'
' 1. Перейдите в <a href = "https://t.me/CryptoBot">криптобота</a>.\n'
' 2. Нажмите /start и затем «кошелек».'
' 3. Пополните баланс кошелька на нужную сумму в любой из трех валют TON, BUSD, BNB (советуем BUSD из-за низких комиссий) или купите валюту в разделе «market».\n'
' 4. Снова перейдите в бота по этой <a href = "http://t.me/CryptoBot?start=IVTpvCfptUL8">ССЫЛКЕ</a>.\n'
' 5. Выберите монету, которой хотите оплатить.\n'
' 6. В комментарии к платежу обязательно укажите ваш контакт телеграмм и адрес кошелька тон, чтобы мы могли с вами связаться и зачислить нфт на маркетплейсе после\n'
'публичного минта.\n'
'\n'
'Адрес бота указывать нельзя. Создайте кошелек tonkeeper или tonwallet или просто'
'укажите ваш контакт в телеграм. После оплаты вы попадете в закрытый чат ранних' 'коллекционеров.'
, parse_mode = types.ParseMode.HTML)
      
    elif message.text == 'Рефералы и ссылка👥':
      status = await bot.get_chat_member(chat_id='-1001235244140', user_id = message.from_user.id)
      if ref_id_count(message.from_user.id) != 0:
        if check_ref_per(message.from_user.id) == 0:
          refs_increase(ref_id_count(message.from_user.id))
          ref_per_increase(message.from_user.id)
          await bot.send_message(ref_id_count(message.from_user.id), 'По вашей ссылке зарегистрировался пользователь!')

      bot_name = 'mjs_ton_bot'
      await bot.send_message(message.from_user.id, text = f'Приглашено рефералов: {count_refs(message.from_user.id)}\n'
f'\n'
f'Ваша реферальная ссылка: \n'
f'{ref_link.format(bot_name, message.from_user.id)}\n'
'\n'
'Условия засчитывания реферала: \n'
'1) Реферал перешел по вашей ссылке нажал /start\n'
'2) Реферал нажал какую нибудь кнопку (для этого нужно подписаться на канал)')
      
    elif message.text == 'Вступить в чат💬':
      if ref_id_count(message.from_user.id) != 0:
        if check_ref_per(message.from_user.id) == 0:
          refs_increase(ref_id_count(message.from_user.id))
          ref_per_increase(message.from_user.id)
          await bot.send_message(ref_id_count(message.from_user.id), 'По вашей ссылке зарегистрировался пользователь!')
          
      await bot.send_message(message.from_user.id, text = '<a href = "https://t.me/metajungles_ru">Нажмите, чтобы вступить в чат 💬</a>', parse_mode = types.ParseMode.HTML)


    elif message.text == 'Посмотреть участников👤':
      if ref_id_count(message.from_user.id) != 0:
        if check_ref_per(message.from_user.id) == 0:
          refs_increase(ref_id_count(message.from_user.id))
          ref_per_increase(message.from_user.id)
          await bot.send_message(ref_id_count(message.from_user.id), 'По вашей ссылке зарегистрировался пользователь!')
      status = await bot.get_chat_member(chat_id='-1001235244140', user_id = message.from_user.id)
      await bot.send_message(message.from_user.id, text = check_table(status))
    
  else:
    await bot.send_message(message.from_user.id, 'Для пользованием бота нужно подписаться на канал: \n'
                           f'{channel_link}')

    
  
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

