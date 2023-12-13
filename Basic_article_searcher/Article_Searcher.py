import advanced
import wikipedia
import customtkinter
from tkinter import END,messagebox


class main:
    def new(self):
        state = self.search_field.get()
        
        try:
            self.result = wikipedia.page(state)
            self.search_result_textbox.configure(state='normal')
            self.search_result_textbox.delete('1.0',END)
            self.search_result_textbox.insert('0.0',self.result.summary)
            self.search_result_textbox.configure(state='disabled')

        except:
            messagebox.showerror("Error","could'n find the article") 

    def advanceee(self):
            
            self.app.destroy()
            a=advanced.advance()


    def __init__(self):

        self.app = customtkinter.CTk()
        self.app.title("Article Searcher")
        self.app.geometry('452x372')
        self.app.resizable(False,False)

        self.search_field = customtkinter.CTkEntry(self.app, placeholder_text="Search articles on wikipedia",height=35,width=350,font=('vendana',15),corner_radius=10)
        self.search_field.place(x=0,y=0)

        self.search_btn=customtkinter.CTkButton(self.app,text='Search',command=self.new,width=100,height=35,corner_radius=10,border_width=1,border_spacing=5,text_color='black',font=('vendana',13,'bold'))
        self.search_btn.place(x=351,y=0)

        self.search_result_textbox = customtkinter.CTkTextbox(master=self.app, width=452,height=300, font=('vendana',17),corner_radius=15,border_width=5,border_spacing=10,state='normal')
        self.search_result_textbox.place(x=0,y=36)
        self.search_result_textbox.insert('0.0','Try running Japan')
        self.search_result_textbox.configure(state='disabled')

        self.btn2=customtkinter.CTkButton(self.app,text='Advanced',command=self.advanceee,width=450,height=35,corner_radius=10,border_width=1,border_spacing=5,text_color='black',font=('vendana',13,'bold'))
        self.btn2.place(x=1,y=337)

        self.app.mainloop()

if __name__=='__main__':

    app=main()
