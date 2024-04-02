import random
import tkinter as tk


def play(action, label, counter):
    if counter < len(action):
        label.configure(image = action[counter])
        counter += 1
        window.after(100,play, idle_to_sleep, label, counter)
    else:
        counter = 0
        window.after(100,play, idle_to_sleep, label, counter)


counter = 0
impath = 'C:\\Users\\troyt\\productivity-pet\\animations\\'
window = tk.Tk()

idle = [tk.PhotoImage(file=impath+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]
sleep = [tk.PhotoImage(file=impath+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]
sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_positive = [tk.PhotoImage(file=impath+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]
walk_negative = [tk.PhotoImage(file=impath+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"100x100+{screen_width - 300}+{screen_height - 150}")
label = tk.Label(window, bd = 0, bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

print(screen_width)
print(screen_height)
window.after(100,play, idle_to_sleep, label, counter)
label.pack()
window.mainloop()



