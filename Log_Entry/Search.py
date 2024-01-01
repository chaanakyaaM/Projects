import os
import customtkinter
from tkinter import END,messagebox

class open_win:

    def __init__(self):
            
            def delete():

                with open("names.txt",'w+') as file:
                    lines=file.readlines()

                    for line in range(len(lines)):
                        if search_entry.get()==line:
                            lines[line]=''
                

                os.remove(f"{self.file_name}.txt")
                self.file_area.configure(state='normal')               
                self.file_area.delete('0.0',END)
                self.file_area.configure(state='disabled') 
                messagebox.showinfo('','Log deleted succesfully.')

            def edit():
                self.file_area.configure(state='normal')
                save_btn=customtkinter.CTkButton(new_name,text="SAVE",command=save,width=100,height=30)
                save_btn.place(x=650,y=650)

            def save():
                text=self.file_area.get(1.0,"end-1c")
                with open(f'{search_entry.get()}.txt','w') as edited_file:
                    edited_file.write(text)
                    edited_file.close()
                messagebox.showinfo('','File successfully edited')

            
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

                    self.file_name=line

                    with open(f"{line}.txt",'r') as found_file:
                        file_content=found_file.read()

                    self.file_area=customtkinter.CTkTextbox(new_name,height=520,width=750,border_color='grey',border_width=1,corner_radius=10)
                    self.file_area.insert('0.0',file_content)
                    self.file_area.configure(state='disabled')
                    self.file_area.place(x=120,y=100)
                    delete_btn=customtkinter.CTkButton(new_name,text="DELETE",command=delete,width=100,height=30)
                    delete_btn.place(x=250,y=650)
                    edit_btn=customtkinter.CTkButton(new_name,text="EDIT",command=edit,width=100,height=30)
                    edit_btn.place(x=650,y=650)

                else:
                    
                    messagebox.showerror("","Log not found")

            new_name=customtkinter.CTk()
            new_name.geometry("1000x700+250+50")
            new_name.resizable(False,False)

            search_label=customtkinter.CTkLabel(new_name,text="Enter the date:",font=('vendana',20))
            search_label.place(x=10,y=10)

            search_entry=customtkinter.CTkEntry(new_name,font=("vendana",15),width=750,placeholder_text='DD-MM-YYYY')
            search_entry.place(x=145,y=12)

            search_btn=customtkinter.CTkButton(new_name,text="SEARCH",command=search,height=30,width=100)
            search_btn.place(x=899,y=10)

            new_name.mainloop()

if __name__=="__main__":
      
      open_win()