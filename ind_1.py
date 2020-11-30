#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 12. Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

from datetime import date
import sys

if __name__ == '__main__':
    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия, Имя ")
            phone = input("Номер телефона ")
            birthday = list(map(int, input("Дата рождения в формате: дд,мм,гггг ").split(',')))

            if 1 >= birthday[1] > 12:
                print("Такого месяца не существует!", file=sys.stderr)
                exit(1)

            if 1 >= birthday[0] > 31:
                print("Такого дня не существует!", file=sys.stderr)
                exit(1)

            today = date.today()
            if birthday[2] > today.year:
                print(f"{birthday[2]} ещё не наступил!", file=sys.stderr)
                exit(1)

            person = {
                'name': name,
                'phone': phone,
                'birthday': birthday,
            }

            people.append(person)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8,
                '-' * 8,
                '-' * 8
            )
            print(line)
            print(
                '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} |'.format(
                    "№",
                    "ФИО",
                    "Номер телефона",
                    "День",
                    "Месяц",
                    "Год"
                )
            )
            print(line)

            for idx, person in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} | {:>8} | {:>8} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('phone', ''),
                        person.get('birthday[0]', ''),
                        person.get('birthday[1]', ''),
                        person.get('birthday[2]', '')
                    )
                )
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            month = int(parts[1])

            count = 0
            for person in people:
                birthday = person.get('birthday', [])
                if birthday:
                    if birthday[1] == month:
                        count += 1
                        print(f'{count}, {person.get("name", "")}')

            if count == 0:
                print(f"Именинников в {month} месяце нетю :(")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <месяц рождения> - дни рождения в текущем месяце;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
