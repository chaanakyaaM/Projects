from tkinter import * 
from tkinter import ttk

class calculator:

    def __init__(self):
        
        root = Tk()
        root.title("simple calculator")

        text1 = Text(root, height=2, width=25,font=("Verdana",20))
        text1.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

        def click(num):
            text1.insert(END,num)

        def addition(alpha):
            num=text1.get("1.0","end-1c")
            global number
            global var
            var="add"
            number=int(num)
            text1.delete("1.0","end")

        def substraction(num):
            num=text1.get("1.0","end-1c")
            global number
            global var
            var="sub"
            number=int(num)
            text1.delete("1.0","end")

        def division():
            num=text1.get("1.0","end-1c")
            global number
            global var
            var="div"
            number=int(num)
            text1.delete("1.0","end")

        def multiplication():
            num=text1.get("1.0","end-1c")
            global number
            global var
            var="mul"
            number=int(num)
            text1.delete("1.0","end")

        def clear():
            text1.delete("1.0", "end")

        def equal():
            thisnum=text1.get("1.0", "end-1c")
            text1.delete("1.0","end-1c")
            if var=="add":
                text1.insert(END,int(number)+int(thisnum))
            elif var=="sub":
                text1.insert(END,int(number)-int(thisnum))
            elif var=="div":
                text1.insert(END,int(number)//int(thisnum))
            elif var=="mul":
                text1.insert(END,int(number)*int(thisnum))

        button_one=ttk.Button(root,text="1",padding=20,command= lambda: click(1))
        button_one.grid(row=1,column=0)

        button_two=ttk.Button(root,text="2",padding=20,command= lambda: click(2))
        button_two.grid(row=1,column=1)

        button_three=ttk.Button(root,text="3",padding=20,command= lambda: click(3))
        button_three.grid(row=1,column=2)

        button_addition=ttk.Button(root,text="+",padding=20,command= lambda: addition('+'))
        button_addition.grid(row=1,column=3)

        button_four=ttk.Button(root,text="4",padding=20,command= lambda: click(4))
        button_four.grid(row=2,column=0)

        button_five=ttk.Button(root,text="5",padding=20,command= lambda: click(5))
        button_five.grid(row=2,column=1)

        button_six=ttk.Button(root,text="6",padding=20,command= lambda: click(6))
        button_six.grid(row=2,column=2)

        button_substract=ttk.Button(root,text="_",padding=20,command= lambda:substraction(40))
        button_substract.grid(row=2,column=3)

        button_seven=ttk.Button(root,text="7",padding=20,command= lambda: click(7))
        button_seven.grid(row=3,column=0)

        button_eight=ttk.Button(root,text="8",padding=20,command= lambda: click(8))
        button_eight.grid(row=3,column=1)

        button_nine=ttk.Button(root,text="9",padding=20,command= lambda: click(9))
        button_nine.grid(row=3,column=2)

        mulbtn=ttk.Button(root,text="x",padding=20,command= multiplication)
        mulbtn.grid(row=3,column=3)

        zero=ttk.Button(root,text="0",padding=20,command= lambda: click(0))
        zero.grid(row=4,column=1)

        equalbtn=ttk.Button(root,text="clear",padding=20,command= clear)
        equalbtn.grid(row=4,column=0)


        button_equal=ttk.Button(root,text="=",padding=20,command= equal)
        button_equal.grid(row=4,column=2)

        button_division=ttk.Button(root,text="/",padding=20,command= division)
        button_division.grid(row=4,column=3)

        root.mainloop()

if __name__=="__main__":

    calculator()