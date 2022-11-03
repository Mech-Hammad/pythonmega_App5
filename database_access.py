import sqlite3

TABLE_NAME = 'book'

def create_table():
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn LONG)" % (TABLE_NAME))
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES ('Apple JUice', 5, 23.5)")
    cur.execute("INSERT INTO %s VALUES (NULL, ?, ?, ?, ?)" % (TABLE_NAME), (title, author, year, isbn)) # either this or above format can be used, we can use string formatting as well if required
    conn.commit()
    conn.close()




def view():
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect
    cur = conn.cursor()
    cur.execute("SELECT * FROM %s" % (TABLE_NAME))
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows

def search(title="", author="", year=0, isbn=0): # Passing default if the user doesn't pass
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect
    cur = conn.cursor()
    # print("SELECT * FROM {0} WHERE title={1} AND author={2} AND year={3} AND isbn={4}".format(TABLE_NAME, title, author, year, isbn)) # Added for debugging
    cur.execute("SELECT * FROM {0} WHERE title='{1}' OR author='{2}' OR year={3} OR isbn={4}".format(TABLE_NAME, title, author, year, isbn))
    rows = cur.fetchall()

    conn.commit()
    conn.close()

    return rows


def delete(id):
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect
    cur = conn.cursor()
    cur.execute("DELETE FROM %s WHERE id=?" % (TABLE_NAME), (id,))

    conn.commit()
    conn.close()



def update(id, title, author, year, isbn):
    conn = sqlite3.connect("lite.db") # Connect to database, if not exist then create new and connect
    cur = conn.cursor()
    cur.execute("UPDATE %s SET title=?, author=?, year=?, isbn=? WHERE id=?" % (TABLE_NAME), (title, author, year, isbn, id))

    conn.commit()
    conn.close()
