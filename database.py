import sqlite3
import tkinter as tk
from datetime import datetime


def deleteDB(conn, table, window_2, event):
    item_selected = table.focus()
    if not item_selected:
        pass
    else:
        item_id = table.item(item_selected)['tags'][0]
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (item_id,))
        conn.commit()
        displayTreeview(conn, table, window_2)


def is_valid_date_format(date_str, date_format):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
# test


def displayTreeview(conn, table, window_2):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY priority ASC, date ASC")
    rows = c.fetchall()

    for item in table.get_children():
        table.delete(item)

    for n in rows:
        sql_date = ""
        id_ = n[0]
        # Convert the string to a datetime object
        if n[1] and is_valid_date_format(n[1], "%m/%d/%y"):
            date_obj = datetime.strptime(n[1], "%m/%d/%y")
            sql_date = date_obj.strftime("%y-%m-%d")
        else:
            pass
        item_id = table.insert(
                "",
                tk.END,
                text = sql_date,
                values = (n[2], n[3], n[4]),
                tags = (id_)
        )
        table.tag_bind(item_id, '<Button-3>', lambda event, item_id=item_id:deleteDB(event, item_id))


def printDB(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    for row in rows:
        print(row)




def clearDB(conn, table, window_2):
    c = conn.cursor()
    c.execute("DELETE FROM tasks")
    conn.commit()
    displayTreeview(conn, table, window_2)


def create_connection(db_file):
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        create_table = """
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                date TEXT,
                priority INTEGER,
                task TEXT,
                notes TEXT
        );"""

        c.execute(create_table)
        conn.commit()

        return conn


def addTodo (conn, table, window_2, date, prio, task, notes):

    c = conn.cursor()
    insert_table = """
        INSERT INTO tasks(date, priority, task, notes)
        VALUES(?, ?, ?, ?)
    """

    c.execute(insert_table, (date, prio, task, notes))
    conn.commit()
    printDB(conn)
    displayTreeview(conn, table, window_2)

    print("add to do")




