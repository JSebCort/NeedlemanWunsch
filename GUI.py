from tkinter import filedialog
from tkinter import *
 
m = Tk()

m.title('Project 2 - NeedlemanWunsch')

m.geometry("600x400+400+100")
#.geometry("window width x window height + position right + position down")

def callback():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File One",filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open(m.filename, 'r') as f:
        file1 = f.read()

def callback1():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File Two",filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open(m.filename, 'r') as f:
        file2 = f.read()


b = Button(m, text="Select", command=callback)
b2 = Button(m, text="Select", command=callback1)
b.pack(anchor =NE, side=TOP, padx=10, pady=10)
b2.pack(anchor =NE, side=TOP, padx= 10, pady=10)

m.mainloop()
