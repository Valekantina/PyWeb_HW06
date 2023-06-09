import sqlite3
import sys

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2 -- Знайти студента із найвищим середнім балом з певного предмета. 
3 -- Знайти середній бал у групах з певного предмета.
4 -- Знайти середній бал на потоці (по всій таблиці оцінок).
5 -- Знайти які курси читає певний викладач.
6 -- Знайти список студентів у певній групі.
7 -- Знайти оцінки студентів у окремій групі з певного предмета.
8 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
9 -- Знайти список курсів, які відвідує студент.
10 -- Список курсів, які певному студенту читає певний викладач.
11 -- Середній бал, який певний викладач ставить певному студентові.
12 -- Оцінки студентів у певній групі з певного предмета на останньому занятті.
"""


def query_sql(file):
    with open(file) as f:
        sql = f.read()

    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def main():
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        result = query_sql(f'query_{task}.sql')
        print(result)


if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        exit()
