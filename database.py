import sqlite3
import tkinter as tk


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

    

def displayTreeview(conn, table, window_2):
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()

    for item in table.get_children():
        table.delete(item)

    for n in rows:
        id_ = n[0]
        item_id = table.insert(
                "",
                tk.END,
                text = n[1],
                values = (n[2]),
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
                name TEXT,
                priority INTEGER
        );"""

        c.execute(create_table)
        conn.commit()

        return conn


def addTodo (conn, table, window_2, task, prio):

    c = conn.cursor()
    insert_table = """
        INSERT INTO tasks(name, priority)
        VALUES(?, ?)
    """

    c.execute(insert_table, (task, prio))
    conn.commit()
    printDB(conn)
    displayTreeview(conn, table, window_2)

    print("add to do")




