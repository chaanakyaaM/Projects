import os
from tkinter import ttk,Tk,Text,END,DISABLED,messagebox

class open_win:

    def __init__(self):
            
            def delete():

                global file_name
                os.remove(f"{file_name}.txt")
            
            def search():
                search_result=search_entry.get()
                j=0

                with open("names.txt",'r') as file:
                    lines=file.readlines()

                    for line in lines:
                        line = line.strip()

                        if (line==search_result):
                            j=1

                            break
                if j==1:

                    global file_name
                    file_name=line
                    search_result_label.config(text="Name found")
                    file_area=Text(new_name)

                    with open(f"{line}.txt",'r') as found_file:
                        file_content=found_file.read()

                    file_area.insert(END,file_content)
                    file_area.config(state=DISABLED)
                    file_area.place(x=120,y=100,height=520,width=750)
                    delete_btn=ttk.Button(new_name,text="DELETE",command=delete)
                    delete_btn.place(x=450,y=650,width=100,height=30)

                else:
                    
                    messagebox.showinfo("","Name not found")

            new_name=Tk()
            new_name.geometry("1000x700+250+50")
            new_name.resizable(False,False)

            search_label=ttk.Label(new_name,text="Enter the date:",font=('vendana',20))
            search_label.place(x=10,y=10)

            search_entry=ttk.Entry(new_name,font=("vendana",20))
            search_entry.place(x=200,y=10,width=350)

            search_btn=ttk.Button(new_name,text="SEARCH",command=search)
            search_btn.place(x=560,y=10,height=40,width=100)

            search_result_label=ttk.Label(new_name,text="",font=("vendana",10,"bold"))
            search_result_label.place(x=10,y=55)

            new_name.mainloop()

if __name__=="__main__":
      
      open_win()