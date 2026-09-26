# 🐍 Vanya OS

**Vanya OS** — Python-десктоп с приложениями, играми, системными инструментами и собственным интерфейсом.

Проект включает классическую desktop-версию и **Vanya OS Mobile Edition** для Android + Termux.

## ✨ Возможности Vanya OS Desktop

- 🖥️ Собственный рабочий стол
- 📁 Explorer / файловый менеджер
- 📝 Заметки
- 🎮 Игры
- 💻 Терминал
- ⚙️ Настройки
- 🔒 Экран блокировки
- 🔍 Поиск
- 🛠️ Системные инструменты
- 🧩 Моды и приложения
- 🎨 Персонализация
- 📌 Панель задач
- 🧰 Большой набор дополнительных функций

## 📱 Vanya OS Mobile Edition

Мобильная версия работает на **Android через Termux и Python**.

### 🚀 Vanya OS Mobile 1.1

В версии 1.1 появились:

- 🎨 4 темы: Neon, Ocean, Sun и Matrix
- 👤 Профиль пользователя
- 🔒 PIN-код и экран блокировки
- 🔋 Информация о батарее через Termux:API
- 🐍 Vanya Python IDE
- 🧩 Пользовательские Python-приложения
- 🛒 Vanya Store
- 📝 Улучшенные заметки
- 🎮 Vanya Arcade
- 🧠 Игра «Ваня Память»
- 📁 Улучшенный файловый менеджер
- 💻 Vanya Terminal
- 🛠️ Информация о системе
- 💾 Информация о диске
- ⚙️ Сохранение настроек
- 🧰 Список всех функций
- ✨ Новое оформление меню

### 📱 Запуск на Android

Для мобильной версии нужен:

- Android
- Termux
- Python 3
- Для функции батареи — Termux:API

После установки Python:

```bash
python3 vanya_mobile_1_1.py
```

Vanya OS Mobile хранит свои настройки и данные в:

```text
~/.vanya_mobile/
```

Пользовательские Python-приложения находятся в:

```text
~/.vanya_mobile/apps/
```

## 🐍 Требования

### Desktop

- Python 3.10+
- Windows / macOS / Linux

### Mobile

- Android
- Termux
- Python 3

## ▶️ Запуск Desktop

### Windows

```text
Vanya_OS_Windows.bat
```

или:

```bash
py vanya_desktop.py
```

### macOS

```text
Vanya_OS.command
```

или:

```bash
python3 vanya_desktop.py
```

### Linux

```bash
./Vanya_OS_Linux.sh
```

или:

```bash
python3 vanya_desktop.py
```

## 📂 Структура проекта

```text
Vanya OS/
├── vanya_desktop.py
├── vanya_os.py
├── vanya_classic.py
├── Vanya_OS_Windows.bat
├── Vanya_OS.command
├── Vanya_OS_Linux.sh
├── wallpaper.png
├── desktop_icons.json
├── mods/
├── notes/
├── users/
├── vanya_apps/
├── eaglercraft/
└── Mobile/
    └── vanya_mobile_1_1.py
```

## 🌐 Eaglercraft

Большой HTML-файл Eaglercraft не включён в публичную GitHub-версию из-за ограничения размера файлов GitHub.

В папке `eaglercraft/` находится информация о том, куда можно поместить соответствующий HTML-файл.

Учитывайте лицензии и права авторов стороннего контента.

## 📜 Лицензия

Проект распространяется под **MIT License**.

Автор: **Vanya** ❤️

---

⭐ Если тебе нравится Vanya OS — поставь звезду репозиторию!

🐍 **Vanya OS — маленькая ОС, созданная на Python.**
