import sqlite3

db = sqlite3.connect('user.db')

# Создание курсора
creat = db.cursor()

#creat.execute("""CREATE TABLE users (
#	name text,
#	surname text,
#	id integer,
#	balance integer,
#	role text
#)""")




creat.execute("INSERT INTO users VALUES ('Pavlik', 'Coca', 100005, 2, 'Наркоша')") 
#creat.execute("DELETE FROM users WHERE rowid = 4")
#creat.execute("UPDATE users SET role = 'Шайтан' WHERE rowid = 3")

creat.execute("SELECT rowid, * FROM users WHERE id > 1")
items = creat.fetchall()
#print(creat.fetchall())
#print(creat.fetchmany())
#print(creat.fetchone()[5])

for el in items:
    print(el[0], el[1], el[2], el[3], el[4], el[5])

db.commit()
db.close()
