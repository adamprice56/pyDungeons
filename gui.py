#!/usr/bin/env python
import tkinter as tk
import menu

def main():
    pass

if __name__ == '__main__':
    main()

def cbc(id, textbox):
    return lambda : callback(id, textbox)

def callback(selection, textbox):
    textToShow = "You Chose: " + selection + "\n"
    textbox.insert(tk.END, textToShow)
    textbox.see(tk.END)             # Scroll if necessary

def updateText(text):
    textbox.insert(tk.END, text)
    textbox.see(tk.END)

top = tk.Tk()
textbox = tk.Text(master=top)
textbox.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)

aButton = tk.Button(bop, text="A", command=cbc("A", textbox))
aButton.pack()

bButton = tk.Button(bop, text="B", command=cbc("B", textbox))
bButton.pack()


tk.Button(bop, text='Exit', command=top.destroy).pack()
#top.after(100, updateText(menu.main))
top.mainloop()