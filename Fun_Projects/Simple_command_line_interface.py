#This is basic command line interface using python

import os
from tkinter import ttk,Text,Tk,END

def new():

    text_result.config(state='normal')
    text_result.delete('1.0',END)
    
    text=text_area.get('1.0','end-1c')
    text_area.delete('1.0',END)
    
    output=os.popen(text).read()
    
    if output=="":
        text_result.insert(END, text+" is not recognized as internal or exernal command.")
        text_result.config(state='disabled')
        
    else:
        text_result.insert(END,'\n'+output)
        text_result.config(state='disabled')

root=Tk()
root.title("Simple command line interface")
root.geometry("700x500+100+200")
root.resizable(False,False)

text_area=Text(root,height=10,font=('vendana',15))
text_area.pack()

btn=ttk.Button(root,text="run",command=new)
btn.place(x=625,y=1,width=75,height=40)

text_result=Text(root)
text_result.place(x=1,y=150,width=800,height=400)
text_result.insert(END,"Try running 'dir' command")

root.mainloop()
