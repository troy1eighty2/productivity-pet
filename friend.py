import random
import tkinter as tk

counter = 0
animation = [0,1,2,3]
impath = 'C:\\Users\\troyt\\productivity-pet\\animations\\'
window = tk.Tk()
screen_width = window.winfo_screenwidth() - 200
screen_height = window.winfo_screenheight() - 150
resolution = [screen_width, screen_height]

def animate(action, event_type, label, counter, response):
    if counter < len(action):
        label.configure(image = action[counter])
        counter += 1
        if event_type == 1:
            resolution[0] -= 10
        elif event_type == 2:
            resolution[0] += 10
        window.geometry(f"100x100+{response[0]}+{response[1]}")
        window.after(100,animate, action, event_type, label, counter, response)
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


