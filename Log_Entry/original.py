from Search import open_win
import customtkinter
import datetime
from tkinter import messagebox
class original_win:

    def __init__(self,name):
        
        self.present=datetime.datetime.now()
        self.name=name
        self.name=customtkinter.CTk()
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)

        def save():

            title=title_entry.get()

            date=str(self.present.date())
            date=date.split('-')
            date.reverse()
            date="-".join(date)


            try:
                with open("names.txt", 'a') as txt_file:#storage of names of saved files with dates
                    txt_file.write(f"{date}\n")
            except:
                with open("names.txt",'w') as txt_file:
                    txt_file.write(f"{date}\n")
            textt=main_text.get(1.0,"end-1c")
            file=open(f"{date}.txt",'w')
            file.write(title+ '\n')
            time=self.present.time()
            t=str(time).split(':')
            file.write(t[0]+':'+t[1]+ '\n')
            file.write(date+ '\n')
            file.write(self.present.strftime("%A")+ '\n')
            file.write(textt+ '\n')

            file.close()

            messagebox.showinfo('',f'Log saves with name {date} successfully.')



        def open_func():

            self.name.destroy()
            open_win()

        title_label=customtkinter.CTkLabel(self.name,text="TITLE:",font=("vendana",15,"bold"))
        title_label.place(x=20,y=15)

        title_entry=customtkinter.CTkEntry(self.name,font=('vendana',20),width=890,height=40,border_color='grey',border_width=2,placeholder_text='Title...')
        title_entry.place(x=80,y=10)

        main_label=customtkinter.CTkLabel(self.name,text="LOG:",font=("vendana",15,"bold"))
        main_label.place(x=20,y=85)

        main_text=customtkinter.CTkTextbox(self.name,font=('vendana',15),height=550,width=890,corner_radius=10,border_color='grey',border_width=2,activate_scrollbars=True)
        main_text.place(x=80,y=80)

        save_btn=customtkinter.CTkButton(self.name,text="SAVE",command=save,height=40,width=70)
        save_btn.place(x=300,y=650)

        open_btn=customtkinter.CTkButton(self.name,text="OPEN",command=open_func,height=40,width=70)
        open_btn.place(x=600,y=650)

        self.name.mainloop()

if __name__=="__main__":
    
    original_win("main")