from tkinter import Tk,Text
from tkinter import ttk
from Search import open_win

class original_win:

    def __init__(self,name):

        self.name=name
        self.name=Tk()
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)

        def save():

            title=title_entry.get()
            time=time_entry.get()
            day=day_entry.get()
            date=date_entry.get()
            date_list=[]
            date_list.append(date)

            try:
                with open("names.txt", 'a') as txt_file:#storage of names of saved files with dates
                    txt_file.write(f"{date}\n")
            except:
                with open("names.txt",'w') as txt_file:
                    txt_file.write(f"{date}\n")
            textt=main_text.get(1.0,"end-1c")
            file=open(f"{date}.txt",'w')
            file.write(title+ '\n')
            file.write(time+ '\n')
            file.write(date+ '\n')
            file.write(day+ '\n')
            file.write(textt+ '\n')

            print("yes")
            file.close()


        def open_func():

            self.name.destroy()
            open_win()

        title_label=ttk.Label(self.name,text="TITLE:",font=("vendana",15,"bold"))
        title_label.place(x=20,y=5)

        title_entry=ttk.Entry(self.name,font=('vendana',20))
        title_entry.place(x=100,y=0,width=890)

        date_label=ttk.Label(self.name,text="DATE:",font=("vendana",15,"bold"))
        date_label.place(x=30,y=55)

        date_entry=ttk.Entry(self.name,font=('vendana',20))
        date_entry.place(x=100,y=45,width=150)

        time_label=ttk.Label(self.name,text="TIME:",font=("vendana",15,"bold"))
        time_label.place(x=30,y=100)

        time_entry=ttk.Entry(self.name,font=('vendana',20))
        time_entry.place(x=100,y=90,width=150)

        day_label=ttk.Label(self.name,text="DAY:",font=("vendana",15,"bold"))
        day_label.place(x=730,y=55)

        day_entry=ttk.Entry(self.name,font=('vendana',20))
        day_entry.place(x=790,y=45,width=200)

        main_text=Text(self.name,font=('vendana',15))
        main_text.place(x=120,y=140,height=500,width=770)

        save_btn=ttk.Button(self.name,text="SAVE",command=save)
        save_btn.place(x=300,y=650,height=40,width=70)

        open_btn=ttk.Button(self.name,text="OPEN",command=open_func)
        open_btn.place(x=600,y=650,height=40,width=70)

        self.name.mainloop()

if __name__=="__main__":
    
    a=original_win("main")