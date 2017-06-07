import tkinter as Tk
import sys
import threading
import menu

root = Tk.Tk()
text = Tk.Text(root)
text.pack()

exit_thread= False
exit_success = False

class Std_redirector(object):
    def __init__(self,widget):
        self.widget = widget

    def write(self,string):
        if not exit_thread:
            self.widget.insert(Tk.END,string)
            self.widget.see(Tk.END)
    def delete(self):
        self.widget.delete(Tk.ALL)

def stop_thread():
    global exit_thread
    exit_thread = True
    if exit_success:
        root.destroy()

def buttonA():
    menu.main("A")
    #menu.determineSelection("A")

def buttonB():
    menu.main("B")
    #menu.determineSelection("B")

button_A = Tk.Button(root,text='A',command=buttonA)
button_A.pack()

button_B = Tk.Button(root,text='B',command=buttonB)
button_B.pack()

exit_button = Tk.Button(root,text='Exit',command=stop_thread)
exit_button.pack()

sys.stdout = Std_redirector(text)

thread1 = threading.Thread(target=menu.menu)
thread1.start()

root.mainloop()

