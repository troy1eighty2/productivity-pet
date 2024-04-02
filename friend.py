import random
import tkinter as tk

counter = 0
animation = [0,1,2,3]
impath = 'C:\\Users\\troyt\\productivity-pet\\animations\\'
window = tk.Tk()
screen_width = window.winfo_screenwidth() - 200
screen_height = window.winfo_screenheight() - 150

def animate(action, label, counter, screen_width, screen_height):
    if counter < len(action):
        label.configure(image = action[counter])
        counter += 1
        window.after(100,animate, action, label, counter,screen_width, screen_height)
    else:
        counter = 0
        return

def event():
    event_type = random.randint(0, 2)
    if event_type == 0:
        window.after(1000,animate, idle, label, counter, screen_width, screen_height)
        window.geometry(f"100x100+{screen_width}+{screen_height}")
    elif event_type == 1:
        window.after(1000,animate, walk_negative, label, counter, screen_width, screen_height)
        window.geometry(f"100x100+{screen_width}+{screen_height}")
    elif event_type == 2:
        window.after(1000,animate, walk_positive, label, counter, screen_width, screen_height)
        window.geometry(f"100x100+{screen_width}+{screen_height}")
    window.after(1000, event)


def destroyWin():
    window.destroy()
    return

idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]
sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]

label = tk.Label(window, bd = 0, bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

window.bind('<Control-k>', destroyWin)
window.after(0, event)
label.pack()
window.mainloop()


