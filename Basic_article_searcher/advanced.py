import wikipedia
import webbrowser
import customtkinter
from tkinter import END,messagebox


class advance:
    def search(self):
        cbox=self.combobox.get()
        state = self.search_field.get()
        
        if cbox=='Hindi':
            wikipedia.set_lang('hi')
        elif cbox=='French':
           wikipedia.set_lang('fr')            
        elif cbox=='Spanish':
            wikipedia.set_lang('es')
        elif cbox=='German':
            wikipedia.set_lang('de')
        elif cbox=='Italian':
            wikipedia.set_lang('it')
        elif cbox=='Russian':
            wikipedia.set_lang('ru')
        elif cbox=='chinese':
            wikipedia.set_lang('zh')
        elif cbox=='Japanese':
            wikipedia.set_lang('ja')
        elif cbox=='Arabic':
            wikipedia.set_lang('ar')
        elif cbox=='English':
            wikipedia.set_lang('en')

        result = wikipedia.page(state) 
            
        self.summary_textbox.configure(state='normal')
        self.summary_textbox.delete('1.0',END)
        self.summary_textbox.insert('0.0',wikipedia.summary(state))
        self.summary_textbox.configure(state='disabled')

        self.title_textbox.configure(state='normal')
        self.title_textbox.delete('1.0',END)
        self.title_textbox.insert('0.0',result.title)
        self.title_textbox.configure(state='disabled')

        self.ubtn.configure(text=f'{result.url}')    

    def url(self):

        state = self.search_field.get()

        try:
            result= wikipedia.page(state)
            webbrowser.open(result.url)

        except:
            messagebox.showerror("Error",'Search field is empty')
                    
    def __init__(self):

        self.app = customtkinter.CTk()
        self.app.title("Advanced Article Search")
        self.app.geometry('652x445')
        self.app.resizable(False,False)

        self.search_field = customtkinter.CTkEntry(self.app, placeholder_text="Search Articles using wikipedia",height=35,width=400,font=('vendana',15),corner_radius=10)
        self.search_field.place(x=0,y=0)

        self.combobox = customtkinter.CTkComboBox(self.app, values=['English','French','Spanish','German','Italian','Russian','Chinese','Japanese','Arabic','Hindi'],height=35,width=145)
        self.combobox.place(x=403,y=1)

        self.btn=customtkinter.CTkButton(self.app,text='Search',command=self.search,height=35,width=100,corner_radius=10,border_width=1,border_spacing=5,text_color='white',font=('vendana',13,'bold'))
        self.btn.place(x=550,y=0)   

        self.title_label=customtkinter.CTkLabel(self.app,text='Title:',font=('vendana',15,'bold'))
        self.title_label.place(x=4,y=40)

        self.title_textbox = customtkinter.CTkTextbox(self.app, width=650,height=10, font=('vendana',14),corner_radius=15,border_width=3,border_spacing=10)
        self.title_textbox.place(x=1,y=70)

        self.summary_label=customtkinter.CTkLabel(self.app,text='Summary:',font=('vendana',15,'bold'))
        self.summary_label.place(x=4,y=125)

        self.summary_textbox = customtkinter.CTkTextbox(self.app, width=650,height=215, font=('vendana',14),corner_radius=15,border_width=3,border_spacing=10)
        self.summary_textbox.place(x=1,y=155)

        self.url_label=customtkinter.CTkLabel(self.app,text='URL:',font=('vendana',15,'bold'))
        self.url_label.place(x=4,y=372)

        self.ubtn=customtkinter.CTkButton(self.app,command=self.url,text='URL is shown here',font=('vendana',15),height=35,width=649,fg_color='transparent',hover_color='grey')
        self.ubtn.place(x=2,y=400)

        self.app.mainloop()

if __name__=='__main__':

    app=advance()
