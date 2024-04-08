import random
import tkinter as tk
from tkinter import ttk
import sqlite3
from database import create_connection, addTodo, clearDB, printDB, displayTreeview, deleteDB

counter = 0
sparkles_counter = 0
animation = [0,1,2,3]
impath = 'C:\\Users\\troyt\\productivity-pet\\animations\\'
window = tk.Tk()
screen_width = window.winfo_screenwidth() - 200
screen_height = window.winfo_screenheight() - 150
resolution = [screen_width, screen_height]
resolution_sparkles = [500,500]
global todo_active
global speech_active
todo_active = False
speech_active = False
window_2 = None
window_3 = None


def animate(action, event_type, label, counter, resolution):
    if counter < len(action):
        label.configure(image = action[counter])
        counter += 1
        if event_type == 1:
            resolution[0] -= 10
        elif event_type == 2:
            resolution[0] += 10
        window.geometry(f"100x100+{resolution[0]}+{resolution[1]}")
        window.after(100,animate, action, event_type, label, counter, resolution)


    else:
        counter = 0
        return

def event():
    event_type = random.randint(0, 3)
    if event_type == 0:
        window.after(1000,animate, idle, event_type, label, counter, resolution)
    elif event_type == 1 and resolution[0] > 150:
        window.after(1000,animate, walk_negative, event_type, label, counter, resolution)
    elif event_type == 2 and resolution[0] < window.winfo_screenwidth() - 199:
        window.after(1000,animate, walk_positive, event_type, label, counter, resolution)
        window.geometry(f"100x100+{resolution[0]}+{resolution[1]}")
    elif event_type == 3:
        window.after(100,animate, idle_to_sleep, event_type, label, counter, resolution)
        window.after(1000,animate, sleep, event_type, label, counter, resolution)
        window.after(7000,animate, sleep_to_idle, event_type, label, counter, resolution)

    if event_type == 3:
        window.after(10000, event)
    else:
        window.after(2000, event)


def destroyWin():
    window.destroy()
    return


def rightClick(event):
    global window_3
    if not window_3:
        window_3 = tk.Toplevel()
        speech_Bubble_Text = tk.Label(window_3, text = "Hello there!")
        speech_Bubble_Text.pack()
    else:
        window_3.destroy()
        window_3 = None


def leftClick(event):
    global window_2
    if not window_2:
        window_2 = tk.Toplevel()
        window_2.geometry(f"+{window_2.winfo_screenwidth()//2}+{window_2.winfo_screenheight()//2}")

        frame_2 = tk.Frame(window_2)
        frame_2.pack(padx = 10, pady = 10)

        window_2.title("To Do List")
        table = ttk.Treeview(frame_2)
        label_sparkles = tk.Label(window_2)
        table.bind("<Double-Button-1>", lambda event:deleteDB(conn,table,event, window_2))
        table.pack()

        add = tk.Button(frame_2, text="Add", command=lambda: addTodo(conn, table, window_2, "task", 1))
        add.pack()
        clear = tk.Button(frame_2, text="Clear", command=lambda: clearDB(conn, table, window_2))
        clear.pack()



        table["columns"] = ("Priority")
        table.column("#0", width = 100)
        table.column("Priority", width = 100)

        table.heading("#0", text="name")
        table.heading("Priority", text="Priority")
        displayTreeview(conn, table, window_2)

    else:
        window_2.destroy()
        window_2 = None

idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]
sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]
sparkles = [tk.PhotoImage(file=impath+'sparkles.gif',format = 'gif -index %i' %(i)) for i in range(26)]

label = tk.Label(window, bd = 0, bg='black')

window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

window.bind('<Control-k>', destroyWin)
# Bind left-click event
window.bind("<Button-1>", leftClick)
# Bind right-click event
window.bind("<Button-3>", rightClick)
window.after(0, event)
label.pack()

print("yo")
conn = create_connection("todo.db")
window.mainloop()



