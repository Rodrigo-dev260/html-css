import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES ('Rodrigo', 46, 'rodrigovai@hotmail.com')")

""" banco.commit() """ 
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())