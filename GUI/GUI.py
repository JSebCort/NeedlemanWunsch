from tkinter import filedialog
from tkinter import *
import BioProject2 as bio
 
m = Tk()

m.title('Project 2 - NeedlemanWunsch')

m.geometry("600x400+400+100")
#.geometry("window width x window height + position right + position down")

file1 = "" 
file2 = "" 

def callback():

    global file1 
    global file2 

    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File One",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file1 = f.read()

def callback1():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File Two",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t2.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file2 = f.read()

main_l = Label(m, text="Needleman-Wunsch Algorithms", font=("Calibri", 16))
l2 = Label(m, text="File Selection")

main_l.pack(anchor =N, side=TOP, pady = 10)
l2.pack(anchor =W, side=TOP,padx=7)

#left hand side text field, buttons, created in order. 
t = Text(m, height=1, width=8)

b = Button(m, text="Select", width=8, command=callback)
b2 = Button(m, text="Select", width=8, command=callback1)

t2 = Text(m, height=1, width=8)


#left hand side textfield, buttons for file openings 
t.pack(anchor =W, side=TOP, padx=10, pady=5)
b.pack(anchor =W, side=TOP, padx=10, pady=5)
t2.pack(anchor =W, side=TOP, padx=10, pady=5)
b2.pack(anchor =W, side=TOP, padx= 10, pady=5)

op = ["Needleman", "Brute Force", "Alg1", "Potato"]
v = StringVar(m)
v.set("Needleman") # default value

l3 = Label(m, text="Choose an Algorithm")
l3.pack(anchor =W, side=TOP,padx=7)

w = OptionMenu(m, v, *op)
w.pack(anchor =W, side=TOP, padx=8, pady=5)

def ok():
    print ("value is: " + v.get())

    if(v.get() == "Brute Force"):
        bio.brutForce(file1, file2)
    if(v.get() == "Needleman"):
        bio.NW(file1,file2)
    if(v.get() == "Alg1"): 
        bio.Pointers(file1, file2)
    if(v.get() == "Potato"): 
        bio.Diagonal(file1, file2)

b3 = Button(m, text="Run", width=8, command=ok)
b3.pack(anchor =W, side=TOP, padx= 10, pady=5)


m.mainloop()