# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:12:46 2019

@author: Kratik Saxena
"""

from Tkinter import *
from tkFileDialog import *

def main():
    
    root = Tk()
    
    root.title("Enter Patents")
        
    L1 = Label(root, text="Patent Numbers (Enter Patent Numbers separated by comma) ")
    L1.grid(row = 0, padx = 2)
    
    T1 = Text(root, height=5, width=40)
    T1.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    T2 = Text(root, height=1, width=40)
    T2.grid(row = 2, column = 2, padx = 5, pady = 5)
    
    L2 = Label(root, text="Select Destination File")
    L2.grid(row = 2, column = 0)
    
    B2 = Button(root,text='Browse',command= lambda: opendialog(T2))
    B2.grid(row = 2, column = 3, padx = 5)
    
    B1 = Button(root, text='Submit',command=lambda: submitpatents_filename (T1, T2))
    B1.grid(row = 5, column = 1, padx = 5, pady = 5)
    
    root.mainloop()
#   print (patents_tuple,filename1)  #just for testing
def submitpatents_filename(T1,T2):
    global patents_tuple
    global filename1
    patents = T1.get("1.0","end-1c")
    patents_tuple = tuple(patents.split(','))    #USE THIS AS FUTURE VARIABLE
    filename1 = T2.get("1.0","end-1c")          #USE THIS AS FUTURE VARIABLE
    return patents_tuple
    return filename1

def opendialog(T2):
    global filename
    filename = askopenfilename(title="Select file")
    T2.insert(0.0, filename)


#
#if __name__ == '__main__':
#    main()