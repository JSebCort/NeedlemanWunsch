from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import BioProject2 as bio
 
m = Tk()

m.title('Project 2 - Bioinformatics')

height=450
width=600

m.geometry("600x470+400+100")
#window width x window height + position right + position down

file1 = "" 
file2 = "" 

def callback():

    global file1 
    global file2 

    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File One",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file1 = f.read()
    

#    for i in file1: 
 #       if(i != 'A' or i != "G" or i != "C" or i != "T"):
  #          file1.replace(i, "-")
   # for i in file2: 
    #    if(i != "A" or i != "G" or i != "C" or i != "T"):
     #      file2.replace(i, "-")

def callback1():
    m.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File Two",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    t2.insert(END, m.filename)
    
    with open(m.filename, 'r') as f:
        file2 = f.read()

main_l = Label(m, text="Alignment Algorithms", font=("Calibri", 16))
main_l.grid(row=1, sticky=N)

canvas_top = Canvas(m, width=600, height=3)
canvas_top.grid(row=2, sticky=N)
canvas_top.create_line(0, 3, width, 3) 

l2 = Label(m, text="File Selection",font=("Calibri", 11))
l2.grid(row=4, sticky=W)

#left hand side text field, buttons, created in order. 
t = Text(m, height=1, width=8)

b = Button(m, text="Select", width=8, command=callback)
b2 = Button(m, text="Select", width=8, command=callback1)

t2 = Text(m, height=1, width=8)


#left hand side textfield, buttons for file openings 
t.grid(row=5, sticky=W)
b.grid(row=6, sticky=W)
t2.grid(row=7, sticky=W)
b2.grid(row=8, sticky=W)

op = ["Needleman", "Brute Force", "Alg1", "Potato"]
v = StringVar(m)
v.set("Needleman") # default value

l3 = Label(m, text="Algorithm",font=("Calibri", 12))
l3.grid(row=9, sticky=W)

w = OptionMenu(m, v, *op)
w.grid(row=10, sticky=W)

label_score = Label(m, text="Scoring",font=("Calibri", 12))
label_score.grid(row=11, sticky=W)

l4 = Label(m, text="Match")
l4.grid(row=12, sticky=W)

t3 = Text(m, height=1, width=8)
t3.grid(row=13, sticky=W)

l4 = Label(m, text="Mismatch")
l4.grid(row=14, sticky=W)

t4 = Text(m, height=1, width=8)
t4.grid(row=15, sticky=W)

l4 = Label(m, text="Output Difference:")
l4.grid(row=4, sticky=N)

t5 = Text(m, height=4, width=40)
t5.grid(row=5, sticky=N)

scroll = Scrollbar(m)
scroll.config(command=t5.yview)
t5.config(yscrollcommand=scroll.set)

l6 = Label(m, text="Score:")
l6.grid(row=6, sticky=N)

t6 = Text(m, height=1, width=8)
t6.grid(row=7, sticky=N)

def run():
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
        #print(bio.score)
        t5.insert(END, bio.best1)
        t6.insert(END, bio.min)

    if(v.get() == "Needleman"):
        #start time
        bio.NW(file1,file2)
        #end time
        t5.insert(END, bio.best1)
        t6.insert(END, bio.min)
    if(v.get() == "Alg1"): 
        bio.Pointers(file1, file2)
        t5.insert(END, bio.best1)
        t6.insert(END, bio.min)
    if(v.get() == "Potato"):
        bio.Diagonal(file1, file2)
        t5.insert(END, bio.best1)
        t6.insert(END, bio.min)

b3 = Button(m, text="Run", width=8, command=run)
b3.grid(row=16, sticky=W)


m.mainloop()