from tkinter import *


root = Tk()

def change():
    text_value = entry1.get()
    color_value = entry2.get()
    
    label.config(text=text_value)
    label.config(fg=color_value)

    label = Label(root, text="", fg="black")
label.pack()

entry1 = Entry(root, width=50, fg="blue", bg="green")
entry1.pack()

entry2 = Entry(root, width=50, fg="black", bg="green")
entry2.pack()

update_button = Button(root, text="Do", command=change)
update_button.pack()



root.mainloop()