import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('crm.db')

# Создаем курсор
cursor = conn.cursor()

# Создаем таблицу "Клиенты"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Клиенты (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Имя TEXT NOT NULL,
        Телефон TEXT,
        Страна TEXT,
        Дата_регистрации DATE
    )
''')

# Создаем таблицу "Задачи"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Задачи (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Название TEXT NOT NULL,
        Описание TEXT,
        Статус TEXT,
        Клиент_ID INTEGER,
        Дата_создания DATE,
        Дата_выполнения DATE,
        FOREIGN KEY (Клиент_ID) REFERENCES Клиенты(ID)
    )
''')

# Создаем таблицу "Страны"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Страны (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Название TEXT NOT NULL
    )
''')

# Вставляем тестовые данные
cursor.execute("INSERT INTO Страны (Название) VALUES ('Россия'), ('Беларусь'), ('США')")
conn.commit()

# Вставляем тестовые данные о клиентах
cursor.execute("""
    INSERT INTO Клиенты (Имя, Телефон, Страна, Дата_регистрации) 
    VALUES 
        ('Иван Иванов', '+79991234567', 'Россия', '2024-03-15'),
        ('Петр Петров', '+79111112233', 'Беларусь', '2024-04-01'),
        ('John Smith', '+11234567890', 'США', '2024-02-20')
        ('Егор Васильев', '+79991231156', 'Россия', '2024-05-23')
""")
conn.commit()

# Вставляем тестовые данные о задачах
cursor.execute("""
    INSERT INTO Задачи (Название, Описание, Статус, Клиент_ID, Дата_создания) 
    VALUES 
        ('Сделать звонок', 'Позвонить Ивану Иванову', 'В процессе', 1, '2024-03-15'),
        ('Отправить письмо', 'Написать письмо Петру Петрову', 'Завершена', 2, '2024-04-02'),
        ('Провести встречу', 'Встретиться с John Smith', 'Планируется', 3, '2024-03-25')
        ('Провести встречу', 'Встретиться с Егор Васильев', 'Планируется', 4, '2024-06-11')
""")
conn.commit()

# Выводим информацию о клиентах
cursor.execute("SELECT * FROM Клиенты")
for row in cursor:
    print(row)

# Выводим информацию о задачах
cursor.execute("SELECT * FROM Задачи")
for row in cursor:
    print(row)

# Выводим информацию о странах
cursor.execute("SELECT * FROM Страны")
for row in cursor:
    print(row)

# Закрываем соединение
conn.close()