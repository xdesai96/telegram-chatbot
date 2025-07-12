# Simple Telegram Chatbot Template

This is a lightweight **Telegram chatbot template** built with [aiogram](https://docs.aiogram.dev/).
It provides a foundation for creating small bots with basic commands and can be easily extended for your own needs.

---

## ✨ Features

* 📜 Predefined commands:

  * `.help` – show all available commands
  * `.info` – get user info
  * `.roll` – roll a dice (1–6)
  * `.coin` – flip a coin (heads/tails)
  * `.weather <city>` – get weather info for a city
  * `.tr <lang>` – translate replied text to specified language
  * `.ping` – check bot latency
  * `.hearts` – animated hearts
  * `.spam <n> <text>` – send `<text>` multiple times
  * `.terminal <cmd>` – execute system commands (for admins)
  * `.uptime` – show bot uptime (for admins)
* 🌐 Simple i18n support (RU & EN out of the box)
* 🔌 Easy to extend with your own commands and logic

---

## 🚀 Getting Started

### Requirements

* Python 3.10+
* A Telegram bot token from [BotFather](https://t.me/BotFather)

### Installation

```bash
git clone https://github.com/xdesai96/telegram-chatbot.git
cd telegram-chatbot
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the bot

```bash
python -m app
```

---

## 📋 To-Do

* 📦 Add database support (e.g., SQLite, PostgreSQL) for:

  * User settings
* 🌍 Add more languages for i18n

---

## 📂 Project Structure

```
app/
├── config.py           # Bot settings
├── handlers/           # Command/callback handlers
├── services/           # API clients, translators, etc.
├── utils/              # Helpers, validators, i18n
├── keyboards/          # Reply keyboards
└── locales/            # en.json, ru.json
```

---

## 🛠 Built With

* [aiogram](https://github.com/aiogram/aiogram) – Telegram Bot API framework
* Python 3.10+
