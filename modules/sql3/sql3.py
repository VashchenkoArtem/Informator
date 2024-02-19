import sqlite3

tabel = sqlite3.connect('admin.db')

cursor = tabel.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS admins (
               id INTEGER PRIMARY KEY, 
               user_id INTEGER NOT NULL,
               email TEXT NOT NULL,
               nickname TEXT NOT NULL,
               password TEXT NOT NULL,
               phone_number TEXT NOT NULL
    )
''')
tabel.commit()

def add_admin(user):
    cursor.execute('''
INSERT INTO admins (
                   user_id, email, nickname, password, phone_number)
                   VALUES (?,?,?,?,?)
''',(user.user_id, user.email, user.nickname, user.password, user.phone_number))
    tabel.commit()