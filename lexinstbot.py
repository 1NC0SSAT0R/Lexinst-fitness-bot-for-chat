import logging
import sqlite3
import random
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "YOUR_API_TOKEN_OF_BOT"

user_last_messages = {}

WELCOME_MESSAGE = """💪 ДОБРО ПОЖАЛОВАТЬ В LEXINST.

Ты сделал свой выбор - стать сильнее. Здесь мы растем вместе.

📋 Доступные команды:
/price – прайс на наши продукты 
/rules – правила нашего чата 
/questions – ответы на часто задаваемые вопросы 
/socialmedia – все наши соц. сети
/biceps – прокачать бицепс
/biceps_top – топ бицепсов этого чата

Просим быть уважительным и соблюдать все правила 😃"""

GOODBYE_MESSAGES = [
    """⚡ ЕЩЁ ОДИН ОТСТУПИЛ...

Сила требует жертв, но не каждый готов платить цену. 
Теряя нас, он теряет часть себя.

Пусть его путь будет долгим, а ноша тяжелой.
Мы же продолжаем расти. Вместе. 💪""",
    
    """🎯 ОН ВЫБРАЛ ИНОЙ ПУТЬ...

Каждое отступление - испытание для оставшихся.
Сила не в количестве, а в верности пути.

Он выбрал иной маршрут. Мы выбираем развитие.
Вперёд, к новым вершинам! 🏔️""",
    
    """🔗 УДАЧИ, БОЕЦ!

Один воин покидает строй. Но сталь закаляется в огне, а не в комфорте.
Его решение - его путь. Наш путь - постоянное преодоление.

Держи форму. Сохраняй фокус. Мы остаемся сильными. 💫""",
    
    """🌑 МЫ ПОТЕРЯЛИ БОЙЦА...

Не каждый выдерживает давление роста. Не каждый готов к ежедневной битве.
Его уход - напоминание: сила требует полной отдачи.

Мы скорбим о потере, но продолжаем тренироваться.
Ибо такова воля стали! ⚔️"""
]

def init_db():
    conn = sqlite3.connect('biceps.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            biceps_size REAL DEFAULT 0,
            last_training TEXT,
            total_trainings INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_user_data(user_id):
    conn = sqlite3.connect('biceps.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_data(user_id, username, first_name, biceps_size, last_training, total_trainings):
    conn = sqlite3.connect('biceps.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users 
        (user_id, username, first_name, biceps_size, last_training, total_trainings)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, username, first_name, biceps_size, last_training, total_trainings))
    conn.commit()
    conn.close()

def get_top_players(limit=10):
    conn = sqlite3.connect('biceps.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, first_name, biceps_size, total_trainings 
        FROM users 
        ORDER BY biceps_size DESC 
        LIMIT ?
    ''', (limit,))
    top_players = cursor.fetchall()
    conn.close()
    return top_players

async def delete_previous_message(user_id: int, chat_id: int, context: CallbackContext):
    if user_id in user_last_messages:
        try:
            await context.bot.delete_message(
                chat_id=chat_id,
                message_id=user_last_messages[user_id]
            )
        except Exception:
            pass
        finally:
            del user_last_messages[user_id]

async def price(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    message = await update.message.reply_text("""💰 Прайс:

🧥 Зип худи - 4990₽
👕 Футболка - 2990₽

Заказать:
http://lexinst.ru""")
    
    user_last_messages[user_id] = message.message_id

async def rules(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    message = await update.message.reply_text("""📜 Правила чата:

❌ не оскорблять участников сообщества
❌ не упоминать религии, нации 
❌ не отправлять материалы 18+
❌ не разжигать конфликты
❌ не рекламировать другие проекты и услуги""")
    
    user_last_messages[user_id] = message.message_id

async def questions(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    keyboard = [
        [InlineKeyboardButton("📦 Сроки отправки и доставки", callback_data="shipping_time")],
        [InlineKeyboardButton("🚚 Как отследить доставку СДЭК", callback_data="track_cdek")],
        [InlineKeyboardButton("💳 Условия оплаты", callback_data="payment_terms")],
        [InlineKeyboardButton("📮 Способы доставки", callback_data="delivery_methods")],
        [InlineKeyboardButton("🔄 Условия возврата", callback_data="return_conditions")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = await update.message.reply_text("❓ Выберите вопрос:", reply_markup=reply_markup)
    
    user_last_messages[user_id] = message.message_id

async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    
    await query.answer()
    
    if query.data == "shipping_time":
        text = """📦 Сроки отправки и доставки:

•Отправка занимает до 10 рабочих дней.
•Доставка зависит от твоего города.
•Предзаказ — до 3-4 недель, дисциплина требует терпения."""
    
    elif query.data == "track_cdek":
        text = """🚚 Как отследить доставку СДЭК:

•Смотри маршрут своей экипировки в личном кабинете СДЭК. 
•Контроль — часть силы."""
    
    elif query.data == "payment_terms":
        text = """💳 Условия оплаты:

•При оформлении заказа можно выбрать удобный способ оплаты: банковские карты, СБП, Tinkoff Pay или SBER Pay.
•Оплата обязательна в полном объеме. Нельзя оплатить при получении."""
    
    elif query.data == "delivery_methods":
        text = """📮 Способы доставки:

📦 СДЭК: в пункт выдачи или прямо в руки курьером."""
    
    elif query.data == "return_conditions":
        text = """🔄 Условия возврата:

•Оформить возврат можно в течении 7 дней с момента получения заказа при условии сохранения его товарного вида: без следов эксплуатации, в первоначальной упаковке(ФЗ о защите прав потребителей ст. 26 1.)"""
    
    else:
        text = "❌ Информация временно недоступна"
    
    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="back_to_questions")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=text, reply_markup=reply_markup)
    user_last_messages[user_id] = query.message.message_id

async def back_button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    
    await query.answer()
    
    keyboard = [
        [InlineKeyboardButton("📦 Сроки отправки и доставки", callback_data="shipping_time")],
        [InlineKeyboardButton("🚚 Как отследить доставку СДЭК", callback_data="track_cdek")],
        [InlineKeyboardButton("💳 Условия оплаты", callback_data="payment_terms")],
        [InlineKeyboardButton("📮 Способы доставки", callback_data="delivery_methods")],
        [InlineKeyboardButton("🔄 Условия возврата", callback_data="return_conditions")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text="❓ Выберите вопрос:", reply_markup=reply_markup)
    user_last_messages[user_id] = query.message.message_id

async def socialmedia(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    message = await update.message.reply_text("""🌐 Наши социальные сети:

🌍 http://lexinst.ru – наш сайт
📱 https://t.me/lexinst – переходник на телеграм канал
🎵 https://www.tiktok.com/@lexinstdd – наш тикток""")
    
    user_last_messages[user_id] = message.message_id

async def commands(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    message = await update.message.reply_text("""🛠️ Доступные команды:

💰 /price – прайс на наши продукты
📜 /rules – правила нашего чата
❓ /questions – ответы на часто задаваемые вопросы
🌐 /socialmedia – все наши соц. сети
💪 /biceps – прокачать бицепс
🏆 /biceps_top – топ игроков
🛠️ /commands – список всех доступных команд""")
    
    user_last_messages[user_id] = message.message_id

async def biceps(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    user = get_user_data(user_id)
    now = datetime.now()
    
    training_messages = [
        "💪 ТЫ ПОДНЯЛ ШТАНГУ НА БИЦЕПС!\nСталь скрипит, мышцы горят... {change} на {amount} см!",
        "🔥 МОЩНЫЙ ПОДХОД С ГАНТЕЛЯМИ!\nПот стекает по вискам... {change} на {amount} см!",
        "🚀 МОЛОТКОВЫЕ СГИБАНИЯ ВЫПОЛНЕНЫ!\nФорма меняется на глазах... {change} на {amount} см!",
        "⚡ КОНЦЕНТРИРОВАННЫЕ СГИБАНИЯ!\nФокус и напряжение... {change} на {amount} см!",
        "🎯 ИДЕАЛЬНАЯ ТЕХНИКА!\nКаждое движение - искусство... {change} на {amount} см!",
        "💥 НОВЫЙ РЕКОРД ПРЕОДОЛЕН!\nБоль - всего лишь иллюзия... {change} на {amount} см!",
        "🌟 СИЛА ПРОРЫВАЕТСЯ НАРУЖУ!\nМышцы отвечают на зов... {change} на {amount} см!",
        "🦾 СТАЛЬНЫЕ ВОЛОКНА УПЛОТНЯЮТСЯ!\nТрансформация неизбежна... {change} на {amount} см!"
    ]
    
    if user:
        last_training = datetime.fromisoformat(user[4])
        if now - last_training < timedelta(hours=24):
            time_left = last_training + timedelta(hours=24) - now
            hours = int(time_left.seconds // 3600)
            minutes = int((time_left.seconds % 3600) // 60)
            
            message_text = f"⏳ ТЫ ЕЩЁ НЕ ВОССТАНОВИЛСЯ, ВОИН!\n"
            message_text += f"Следующее испытание через {hours}ч {minutes}м\n"
            message_text += f"📊 Твой текущий бицепс: {user[3]:.1f} см\n"
            message_text += f"🎯 Всего преодолений: {user[5]}"
            
            message = await update.message.reply_text(message_text)
            user_last_messages[user_id] = message.message_id
            return
    
    growth = random.randint(-20, 20)
    current_biceps = user[3] if user else 0
    new_biceps = max(0, current_biceps + growth)
    total_trainings = (user[5] if user else 0) + 1
    
    change_word = "вырос" if growth > 0 else "уменьшился" if growth < 0 else "не изменился"
    change_emoji = "📈" if growth > 0 else "📉" if growth < 0 else "➡️"
    
    training_message = random.choice(training_messages)
    message_text = training_message.format(change=change_word, amount=abs(growth))
    message_text += f"\n\n{change_emoji} ТВОЙ БИЦЕПС: {new_biceps:.1f} см"
    message_text += f"\n🎯 ВСЕГО ПРЕОДОЛЕНИЙ: {total_trainings}"
    
    if growth > 15:
        message_text += "\n\n🎉 НЕВЕРОЯТНО! ТЫ РВЁШЕШЬ ПРЕДЕЛЫ! 💪"
    elif growth < -15:
        message_text += "\n\n😔 ПЛОХОЙ ДЕНЬ... НО ЗАВТРА ТЫ ВЕРНЁШЬСЯ СИЛЬНЕЕ!"
    
    update_user_data(
        user_id=user_id,
        username=update.effective_user.username,
        first_name=update.effective_user.first_name,
        biceps_size=new_biceps,
        last_training=now.isoformat(),
        total_trainings=total_trainings
    )
    
    message = await update.message.reply_text(message_text)
    user_last_messages[user_id] = message.message_id

async def biceps_top(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    await delete_previous_message(user_id, chat_id, context)
    
    top_players = get_top_players(10)
    
    if not top_players:
        message = await update.message.reply_text("🏆 ЗАЛ СЛАВЫ ПУСТ!\nБудь первым, кто оставит свой след! 💪")
        user_last_messages[user_id] = message.message_id
        return
    
    message_text = "🏆 ТАБЛИЦА ЛИДЕРОВ LEXINST 💪\n\n"
    
    for i, (username, first_name, biceps_size, trainings) in enumerate(top_players, 1):
        name = f"@{username}" if username else first_name
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        message_text += f"{medal} {name} - {biceps_size:.1f} см ({trainings} испытаний)\n"
    
    message_text += "\n💪 СИЛА ИМЕЕТ ИМЯ!"
    message = await update.message.reply_text(message_text)
    user_last_messages[user_id] = message.message_id

async def welcome_new_member(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        await update.message.reply_text(WELCOME_MESSAGE)

async def goodbye_member(update: Update, context: CallbackContext) -> None:
    if update.message.left_chat_member:
        goodbye_message = random.choice(GOODBYE_MESSAGES)
        await update.message.reply_text(goodbye_message)

def main() -> None:
    init_db()
    
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("price", price))
    application.add_handler(CommandHandler("rules", rules))
    application.add_handler(CommandHandler("questions", questions))
    application.add_handler(CommandHandler("socialmedia", socialmedia))
    application.add_handler(CommandHandler("commands", commands))
    application.add_handler(CommandHandler("biceps", biceps))
    application.add_handler(CommandHandler("biceps_top", biceps_top))
    
    application.add_handler(CallbackQueryHandler(button_handler, pattern="^(shipping_time|track_cdek|payment_terms|delivery_methods|return_conditions)$"))
    application.add_handler(CallbackQueryHandler(back_button_handler, pattern="^back_to_questions$"))
    
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    application.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye_member))

    application.run_polling()

if __name__ == '__main__':
    main()= '__main__':
    main()