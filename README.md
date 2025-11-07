# Lexinst bot for chat in Telegram💪

[English](#english) | [Русский](#russian)

---

## English {#english}

> ⚠️ **Project Status**: Cancelled by client  
> This project was developed by request but subsequently cancelled. The code is published for portfolio and educational purposes.

### Overview

A Telegram bot for fitness community management with gamification elements. Designed for the LEXINST brand to engage community members through interactive features while providing essential information about products and services.

### Features

#### 🤖 Core Functionality
- **Product Information** - Price lists and product details
- **Community Rules** - Chat guidelines and regulations
- **Interactive FAQ** - Inline keyboard-based question system
- **Social Media Links** - Direct links to all brand platforms

#### 🎮 Gamification System
- **Biceps Training Game** - Virtual muscle growth simulation
- **Leaderboard** - Top players ranking
- **Training Cooldown** - 24-hour limit between sessions
- **Progress Tracking** - SQLite database for user statistics

#### 👥 Community Management
- **Auto Welcome** - Greeting new members
- **Farewell Messages** - Random goodbye messages for leaving members
- **Message Management** - Automatic cleanup of previous commands

### Technology Stack

- **Python 3.x**
- **python-telegram-bot** - Telegram Bot API wrapper
- **SQLite3** - Database for user progress
- **Logging** - Comprehensive event tracking

### Installation

1. **Clone repository**
```bash
git clone https://github.com/1NC0SSAT0R/Lexinst-fitness-bot-for-chat.git
cd Lexinst-fitness-bot-for-chat
```

2. **Install dependencies**
```bash
pip install python-telegram-bot
```

3. **Configure bot**
   - Obtain Bot Token from [@BotFather](https://t.me/BotFather)
   - Replace `YOUR_API_TOKEN_OF_BOT` in the code with your actual token

4. **Run bot**
```bash
python lexinstbot.py
```

### Business Model

The bot serves as an **information platform** - it provides product details, pricing, and brand information while directing actual purchases to the main website. This approach maintains community engagement while driving traffic to primary sales channels.

**Key points:**
- Bot provides product information only
- All orders are processed through the main website
- Focus on community building and brand loyalty
- Gamification increases user retention

### Commands Reference

| Command | Description |
|---------|-------------|
| `/start` | Initialize bot |
| `/price` | Product prices and ordering info |
| `/rules` | Community guidelines |
| `/questions` | Interactive FAQ with buttons |
| `/socialmedia` | Social media links |
| `/biceps` | Train your virtual biceps |
| `/biceps_top` | Leaderboard top players |
| `/commands` | Available commands list |

### Project Structure

```
lexinst-bot/
├── lexinstbot.py       # Main bot implementation
├── biceps.db           # SQLite database (auto-generated)
└── README.md          # Documentation
```

### Disclaimer

This project was developed by client request but was cancelled before full deployment. The code is provided as-is for educational purposes and portfolio demonstration.

### Contact

Developer: [Telegram](https://t.me/inc0bio)

---

## Русский {#russian}

> ⚠️ **Статус проекта**: Отменен заказчиком  
> Данный проект был разработан по запросу, но впоследствии отменен. Код публикуется для портфолио и образовательных целей.

### Обзор

Telegram бот для управления фитнес-сообществом с элементами геймификации. Разработан для бренда LEXINST для вовлечения участников сообщества через интерактивные функции while предоставления основной информации о продуктах и услугах.

### Функционал

#### 🤖 Основные возможности
- **Информация о продуктах** - Прайсы и описание товаров
- **Правила сообщества** - Правила чата и рекомендации
- **Интерактивный FAQ** - Система вопросов с инлайн-кнопками
- **Ссылки на соцсети** - Прямые ссылки на все платформы бренда

#### 🎮 Игровая система
- **Игра "Бицепс"** - Виртуальная прокачка мышц
- **Таблица лидеров** - Рейтинг лучших игроков
- **Время восстановления** - Лимит 24 часа между тренировками
- **Отслеживание прогресса** - База данных SQLite для статистики пользователей

#### 👥 Управление сообществом
- **Автоприветствие** - Приветствие новых участников
- **Прощальные сообщения** - Случайные сообщения при выходе
- **Управление сообщениями** - Автоматическая очистка предыдущих команд

### Технологический стек

- **Python 3.x**
- **python-telegram-bot** - Обертка для Telegram Bot API
- **SQLite3** - База данных для прогресса пользователей
- **Logging** - Комплексное отслеживание событий

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/1NC0SSAT0R/Lexinst-fitness-bot-for-chat.git
cd Lexinst-fitness-bot-for-chat
```

2. **Установите зависимости**
```bash
pip install python-telegram-bot
```

3. **Настройте бота**
   - Получите токен бота у [@BotFather](https://t.me/BotFather)
   - Замените `YOUR_API_TOKEN_OF_BOT` в коде на ваш реальный токен

4. **Запустите бота**
```bash
python lexinstbot.py
```

### Бизнес-модель

Бот служит **информационной платформой** - он предоставляет информацию о продуктах, ценах и бренде, перенаправляя реальные заказы на основной сайт. Такой подход поддерживает вовлеченность сообщества while направляя трафик в основные каналы продаж.

**Ключевые моменты:**
- Бот предоставляет только информацию о продуктах
- Все заказы обрабатываются через основной сайт
- Фокус на построение сообщества и лояльности бренду
- Геймификация увеличивает удержание пользователей

### Справочник команд

| Команда | Описание |
|---------|-------------|
| `/start` | Инициализация бота |
| `/price` | Цены на продукты и информация о заказе |
| `/rules` | Правила сообщества |
| `/questions` | Интерактивный FAQ с кнопками |
| `/socialmedia` | Ссылки на соцсети |
| `/biceps` | Тренировка виртуального бицепса |
| `/biceps_top` | Таблица лидеров |
| `/commands` | Список доступных команд |

### Структура проекта

```
lexinst-bot/
├── lexinstbot.py       # Основная реализация бота
├── biceps.db           # SQLite база данных (авто-генерация)
└── README.md          # Документация
```

### Отказ от ответственности

Этот проект был разработан по запросу заказчика, но отменен до полного развертывания. Код предоставляется "как есть" для образовательных целей и демонстрации в портфолио.

### Контакты

Разработчик: [Telegram](https://t.me/inc0bio)
