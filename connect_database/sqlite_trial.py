import sqlite3
import pandas as pd
print(sqlite3.version)
print(sqlite3.sqlite_version)

#connect db to memory
db = sqlite3.connect(':memory:')
cursor = db.cursor()

# create the format of table
cursor.execute("""CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, price TEXT, year TEXT)""")
db.commit()
# insert info
cursor.execute("""INSERT INTO books values (1, "Pro Powershow", "Bryan Cafferky", 35.00, 2015)""")
cursor.execute("""INSERT INTO books values (2, "Hithiker's Guide to the Galaxy", "Douglas Adas", 12.00, 199)""")
db.commit()
# method 1 => list
lstbooks = cursor.execute("""select * from books;""").fetchall()
db.commit()
print(lstbooks)
print(type(lstbooks))

# method 2 => dataframe
dfbook = pd.read_sql_query("select * from books", db)
print(dfbook)
print(type(dfbook))
# drop table
cursor = db.cursor()
cursor.execute("""DROP TABLE books""")
db.commit()
empty_booksdf = cursor.execute("""select * from books;""").fetchall()
db.commit()
print(empty_booksdf)

# ----------------------------------------------------------------------------------

# connect to chinook
conn = sqlite3.connect("chinook.db")
cur = conn.cursor()

albums = cur.execute("""select * from albums order by title limit 3;""").fetchall()
print(albums)
