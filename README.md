# GOIT-Python_Web-HW-6

## Основне завдання

Реалізуйте базу даних, схема якої містить:

**Таблиця студентів;\*
**Таблицю груп;_
\*\*Таблицю викладачів;_
**Таблицю предметів із вказівкою викладача, який читає предмет;\*
**Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано;\*
Заповніть отриману базу даних випадковими даними (~30-50 студентів, 3 групи, 5-8 предметів, 3-5 викладачів, до 20 оцінок у кожного студента з усіх предметів). Використовуйте пакет Faker для наповнення.

Зробити такі вибірки з отриманої бази даних:

1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2. Знайти студента із найвищим середнім балом з певного предмета.
3. Знайти середній бал у групах з певного предмета.
4. Знайти середній бал на потоці (по всій таблиці оцінок).
5. Знайти які курси читає певний викладач.
6. Знайти список студентів у певній групі.
7. Знайти оцінки студентів у окремій групі з певного предмета.
8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
9. Знайти список курсів, які відвідує студент.
10. Список курсів, які певному студенту читає певний викладач.
    Для кожного запиту оформити окремий файл query_number.sql, де замість number підставити номер запиту. Файл містить SQL інструкцію, яку можна виконати як у терміналі бази даних, так і через cursor.execute(sql)

## Додаткове завдання

Для додаткового завдання зробіть такі запити підвищеної складності:

11. Середній бал, який певний викладач ставить певному студентові.
12. Оцінки студентів у певній групі з певного предмета на останньому занятті.