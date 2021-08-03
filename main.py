import time
from tkinter import *

# settings
lbl_settings = ("Arial", 8)
typed_text = "I think I am a really fast typer on my keyboard!?"
d_time_start = 0.0

# functions
def press_start():
    global d_time_start
    d_time_start = time.time()
    btn_start.config(state=DISABLED)
    btn_stop.config(state=NORMAL)
    input_text.config(state=NORMAL)
    input_text.focus()

def press_stop():
    final_time = time.time() - d_time_start
    btn_stop.config(state=DISABLED)
    input_text.config(state=DISABLED)

    if input_text.get() == typed_text:
        lbl_bottom.config(text=f"Das war super! Du hast {round(final_time, 2)} Sek. benötigt!", fg='#0ac42f')
    else:
        lbl_bottom.config(text="Sorry, aber du hast den Satz falsch geschrieben! Noch einmal?", fg='#d6290b')

# create window
window = Tk()
window.title("Measure speed of typing")
window.eval('tk::PlaceWindow . center')
window.config(padx=25, pady=25)

# label
lbl_top = Label(text="Try to write the following sentence as fast as you can: 'I think I am a really fast typer on my keyboard!?'", font=lbl_settings)
lbl_top.grid(column=0, row=0, columnspan=2)
lbl_bottom = Label(text="")
lbl_bottom.grid(column=0, row=3, columnspan=2)

# input
input_text = Entry(state=DISABLED)
input_text.grid(column=0, row=1, columnspan=2, sticky="ew")

# buttons
btn_start = Button(text="Start", command=press_start)
btn_start.grid(column=0, row=2, sticky="ew", padx=10, pady=10)
btn_stop = Button(text="Stop", state=DISABLED, command=press_stop)
btn_stop.grid(column=1, row=2, sticky="ew", padx=10, pady=10)

# open window at execution
window.mainloop()
