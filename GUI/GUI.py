from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import BioProject2 as bio
 
m = Tk()

m.title('Project 2 - Bioinformatics')

height=450
width=600

m.geometry("600x470+400+100")
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

main_l = Label(m, text="Alignment Algorithms", font=("Calibri", 16))
main_l.pack(anchor =N, side=TOP, pady = 10)

canvas_top = Canvas(m, width=600, height=3)
canvas_top.pack()

canvas_top.create_line(0, 3, width, 3) 



l2 = Label(m, text="File Selection",font=("Calibri", 11))
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

l3 = Label(m, text="Algorithm",font=("Calibri", 12))
l3.pack(anchor =W, side=TOP,padx=7,pady = 3)

w = OptionMenu(m, v, *op)
w.pack(anchor =W, side=TOP, padx=8, pady=5)

label_score = Label(m, text="Scoring",font=("Calibri", 12))
label_score.pack(anchor =W, side=TOP, padx=7, pady = 3)

l4 = Label(m, text="Match")
l4.pack(anchor =W, side=TOP,padx=7)

t3 = Text(m, height=1, width=8)
t3.pack(anchor =W, side=TOP, padx=10, pady=5)

l4 = Label(m, text="Mismatch")
l4.pack(anchor =W, side=TOP,padx=7)

t4 = Text(m, height=1, width=8)
t4.pack(anchor =W, side=TOP, padx=10, pady=5)

def ok():
    print ("value is: " + v.get())
    
    try:  
        score = int(t3.get("1.0",'end-1c')) 
    except ValueError:
        messagebox.showerror("Error", "A number was not entered or there was an empty field.")

    try: 
        mismatch = int(t4.get("1.0",'end-1c'))
    except ValueError:
        messagebox.showerror("Error", "A number was not entered or there was an empty field.")

    if(v.get() == "Brute Force"):
        bio.brutForce(file1, file2)
    if(v.get() == "Needleman"):
        #start time
        bio.NW(file1,file2)
        #end time
    if(v.get() == "Alg1"): 
        bio.Pointers(file1, file2)
    if(v.get() == "Potato"): 
        bio.Diagonal(file1, file2)

    

b3 = Button(m, text="Run", width=8, command=ok)
b3.pack(anchor =W, side=TOP, padx= 10, pady=5)


m.mainloop()