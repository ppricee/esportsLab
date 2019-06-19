import tkinter as tk

def pc_active():
    print("This PC is Active")

def pc_unactive():
    print("PC not active")

root = tk.Tk()

#Label for buttons
question = tk.Label(root, text="Is this PC active?")
question.pack(side=tk.TOP)

frame = tk.Frame(root, height=100, width=100)
frame.pack_propagate(0)
frame.pack()



button = tk.Button(frame,
                   text="NO",
                   padx=5,
                   pady=5,
                   fg="red",
                   command=pc_unactive)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Yes",
                   padx=5,
                   pady=5,
                   command=pc_active)
slogan.pack(side=tk.LEFT)




root.mainloop()