from tkinter import filedialog
from tkinter import *
 
m = Tk()

m.title('Project 2 - NeedlemanWunsch')

m.geometry("600x400+400+100")
#.geometry("window width x window height + position right + position down")

def callback():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File One",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file1 = f.read()

def callback1():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File Two",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t2.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file2 = f.read()

l = Label(m, text="File Selection")

l.pack(anchor =E, side=TOP,padx=7)

#left hand side text field, buttons, created in order. 
t = Text(m, height=1, width=8)

b = Button(m, text="Select", width=8, command=callback)
b2 = Button(m, text="Select", width=8, command=callback1)

t2 = Text(m, height=1, width=8)


#left hand side textfield, buttons for file openings 
t.pack(anchor =E, side=TOP, padx=10, pady=5)
b.pack(anchor =E, side=TOP, padx=10, pady=5)
t2.pack(anchor =E, side=TOP, padx=10, pady=5)
b2.pack(anchor =NE, side=TOP, padx= 10, pady=5)

m.mainloop()
