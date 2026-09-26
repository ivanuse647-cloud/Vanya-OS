#!/usr/bin/env python3

import os
import platform
import sys
from datetime import datetime

APP_NAME = "VANYA OS MOBILE EDITION"
VERSION = "1.0"


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def pause():
    input("\nНажми Enter, чтобы вернуться в меню...")


def show_header():
    print(APP_NAME)
    print(f"Версия {VERSION}")
    print("-" * 50)


def files():
    clear_screen()
    show_header()
    print("📁 ФАЙЛЫ")
    print("-" * 50)
    print("Текущая папка:", os.getcwd())
    print("\nСодержимое:")
    try:
        for item in os.listdir():
            print("  •", item)
    except OSError as error:
        print("Ошибка:", error)
    pause()


def notes():
    clear_screen()
    show_header()
    print("📝 ЗАМЕТКИ")
    print("-" * 50)
    text = input("Напиши заметку: ")

    if text.strip():
        with open("vanya_notes.txt", "a", encoding="utf-8") as file:
            file.write(text.strip() + "\n")
        print("\n✓ Заметка сохранена в vanya_notes.txt")
    else:
        print("\nЗаметка пустая.")
    pause()


def games():
    clear_screen()
    show_header()
    print("🎮 ИГРЫ")
    print("-" * 50)
    print("1 - Камень, ножницы, бумага")
    print("2 - Угадай число")
    print("3 - Назад")

    choice = input("\nВыбери игру: ").strip()

    if choice == "1":
        print("\n🚧 Игра пока в разработке!")
    elif choice == "2":
        print("\n🚧 Игра пока в разработке!")
    elif choice != "3":
        print("\nНеизвестная игра.")

    if choice != "3":
        pause()


def calculator():
    clear_screen()
    show_header()
    print("🧮 КАЛЬКУЛЯТОР")
    print("-" * 50)
    print("Примеры: 2 + 2, 10 * 5, 20 / 4")
    print("Для выхода напиши: exit")

    while True:
        expression = input("\n>>> ").strip()
        if expression.lower() == "exit":
            break

        allowed = set("0123456789+-*/().% ")
        if not expression or any(char not in allowed for char in expression):
            print("Можно использовать только числа и + - * / % ( ).")
            continue

        try:
            result = eval(expression, {"__builtins__": {}}, {})
            print("=", result)
        except Exception:
            print("Ошибка вычисления.")


def terminal():
    clear_screen()
    show_header()
    print("💻 VANYA TERMINAL")
    print("-" * 50)
    print("Команды выполняются через систему Android/Termux.")
    print("exit — назад в Vanya OS.")

    while True:
        command = input("\nVanya $ ").strip()
        if command.lower() == "exit":
            break
        if command:
            os.system(command)


def settings():
    clear_screen()
    show_header()
    print("⚙️ НАСТРОЙКИ")
    print("-" * 50)
    print("1 - Версия Vanya OS")
    print("2 - Платформа")
    print("3 - Время")
    print("4 - Назад")

    choice = input("\nВыбери пункт: ").strip()

    if choice == "1":
        print(f"\nVanya OS Mobile Edition {VERSION}")
    elif choice == "2":
        print(f"\nПлатформа: {platform.platform()}")
        print(f"Python: {platform.python_version()}")
    elif choice == "3":
        print(f"\nСейчас: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    elif choice != "4":
        print("\nНеизвестный пункт.")

    if choice != "4":
        pause()


def all_functions():
    clear_screen()
    show_header()
    print("🧰 ВСЕ ФУНКЦИИ")
    print("-" * 50)
    print("1 - Файлы")
    print("2 - Заметки")
    print("3 - Игры")
    print("4 - Калькулятор")
    print("5 - Терминал")
    print("6 - Настройки")
    print("7 - Информация о системе")
    pause()


def system_info():
    clear_screen()
    show_header()
    print("🖥️ ИНФОРМАЦИЯ О СИСТЕМЕ")
    print("-" * 50)
    print(f"ОС: {platform.system()} {platform.release()}")
    print(f"Архитектура: {platform.machine()}")
    print(f"Python: {platform.python_version()}")
    print(f"Папка: {os.getcwd()}")
    print(f"Время: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    pause()


def store():
    clear_screen()
    show_header()
    print("🛒 VANYA STORE")
    print("-" * 50)
    print("Магазин пока пуст.")
    print("Скоро здесь появятся приложения и моды!")
    pause()


def main():
    while True:
        clear_screen()
        show_header()

        print("1 - Файлы")
        print("2 - Заметки")
        print("3 - Игры")
        print("4 - Калькулятор")
        print("5 - Терминал")
        print("6 - Настройки")
        print("7 - Все функции")
        print("8 - Информация о системе")
        print("9 - Vanya Store")
        print("10 - Выход")

        print("-" * 50)
        choice = input("Выбери название функции: ").strip()

        if choice == "1":
            files()
        elif choice == "2":
            notes()
        elif choice == "3":
            games()
        elif choice == "4":
            calculator()
        elif choice == "5":
            terminal()
        elif choice == "6":
            settings()
        elif choice == "7":
            all_functions()
        elif choice == "8":
            system_info()
        elif choice == "9":
            store()
        elif choice == "10":
            clear_screen()
            print(APP_NAME)
            print("До встречи! 👋")
            break
        else:
            print("\n❌ Такой функции нет.")
            input("Нажми Enter...")


if __name__ == "__main__":
    main()
