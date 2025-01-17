# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:57:53 2019

@author: Kratik Saxena
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:12:46 2019
@author: Kratik Saxena
"""

from Tkinter import *
from tkFileDialog import *
from ScrolledText import *

def main():


    root = Tk()
    
    root.title("Enter Patents")
    
    L4 = Label(root, text="Choose One:", font=("Helvetica", 10))
    L4.grid(row = 0, padx = 2)
    
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    
    C1 = Checkbutton(root, text = "Download Bibliographic in Excel", variable = CheckVar1, font=("Helvetica", 10))
    C1.grid(row = 0, column = 1, pady = 5)
    
    C2 = Checkbutton(root, text = "Automate Report", variable = CheckVar2, font=("Helvetica", 10))
    C2.grid(row = 0, column = 2, pady = 5)
    
    
    #Note for comma
    Note1 = Label(root, text="Note: Separate Patent Numbers by comma ( , )", font=("Helvetica", 10), fg="Red")
    Note1.grid(row = 2, column = 1, padx = 2)
    
    #Primary patent field
    T1 = ScrolledText(root, height = 8, width = 50)
    T1.grid(row = 3, column = 1, padx = 5, pady = 5)
    
    L1 = Label(root, text="Primary (X) Patent Numbers", font=("Helvetica", 10))
    L1.grid(row = 3, padx = 2)
    
    #Secondary patent field
    T2 = ScrolledText(root, height = 8, width = 50)
    T2.grid(row = 4, column = 1, padx = 5, pady = 5)
    
    L2 = Label(root, text="Secondary (Y) Patent Numbers", font=("Helvetica", 10))
    L2.grid(row = 4, padx = 2)
    
    #Select file field
    T3 = Text(root, height=1.25, width=52)
    T3.grid(row = 5, column = 1, padx = 5, pady = 5)
    
    L3 = Label(root, text="Select Destination File", font=("Helvetica", 10))
    L3.grid(row = 5, column = 0)
    
    B2 = Button(root,text='Browse',command= lambda: opendialog(T3))
    B2.grid(row = 5, column = 3, padx = 10)
    
    B1 = Button(root, text='Submit',command=lambda: submitpatents_filename (T1, T2, T3, root))
    B1.grid(row = 6, column = 1, padx = 5, pady = 10)
    
    root.mainloop()
    return patents_tuple_X, patents_tuple_Y, filename1, CheckVar1.get(), CheckVar2.get()
#print (patents_tuple_X, patents_tuple_Y, filename1, CheckVar1.get(), CheckVar2.get())


def submitpatents_filename(T1,T2,T3,root):
    global patents_tuple_X, patents_tuple_Y
    global filename1
    patents_X = T1.get("1.0","end-1c")
    patents_Y = T2.get("1.0","end-1c")
    patents_tuple_X = tuple(patents_X.split(','))    #USE THIS AS FUTURE VARIABLE
    patents_tuple_Y = tuple(patents_Y.split(','))    #USE THIS AS FUTURE VARIABLE
    filename1 = T3.get("1.0","end-1c")          #USE THIS AS FUTURE VARIABLE
    root.destroy()
    return patents_tuple_X, patents_tuple_Y, filename1
#    print (patents_tuple_X, patents_tuple_Y, filename1)

def opendialog(T3):
    global filename
    filename = askopenfilename(title="Select file")
    T3.insert(0.0, filename)