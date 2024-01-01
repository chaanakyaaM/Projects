import MAIN
from tkinter import messagebox
import cryptocode
import customtkinter

class signup:

    def __init__(self,name="Sign up"):
        
        self.name=name
        self.name=customtkinter.CTk()
        self.name.title(name)
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)

        def sign_up():

            user_name=username.get()
            pass_word=password.get()

            encrypted_username=cryptocode.encrypt(user_name,pass_word)

            encrypted_password=cryptocode.encrypt(pass_word,user_name)
            # print(encrypted_password)
            # print(encrypted_username)


            #username
            #password

            repassword.configure(show="")
            re_pass_word=repassword.get()
            repassword.configure(show="*")

            if pass_word==re_pass_word:

                try:
                    file=open("encrypted_usernames_passwords.txt",'a')

                except:
                    file=open("encrypted_usernames_passwords.txt",'w')

                file.write(encrypted_username + "," + encrypted_password+"\n")
                file.close()

                self.name.destroy()
                MAIN.login()

            else:
                messagebox.showinfo("","check and re-enter the password correctly")
            
        div_area=customtkinter.CTkTextbox(self.name,state='disabled',height=200,width=500,corner_radius=10,border_color='white',border_width=1,fg_color='black')
        div_area.place(x=240,y=180)

        username_label=customtkinter.CTkLabel(self.name,text="Username:",font=("vendana",15,'bold'),height=30,width=110,fg_color='black')
        username_label.place(x=330,y=230)

        username=customtkinter.CTkEntry(self.name,font=('vendana',15),height=30,width=170,fg_color='transparent')
        username.place(x=440,y=231)

        password_label=customtkinter.CTkLabel(self.name,text="Password:",font=("vendana",15,'bold'),height=30,width=110,fg_color='black')
        password_label.place(x=330,y=270)

        password=customtkinter.CTkEntry(self.name,font=('vendana',15,'bold'),height=30,width=170,fg_color='transparent')
        password.place(x=440,y=270)

        repassword_label=customtkinter.CTkLabel(self.name,text="Confirm:",font=("vendana",15,'bold'),height=30,width=110,fg_color='black')
        repassword_label.place(x=330,y=310)

        repassword=customtkinter.CTkEntry(self.name,font=('vendana',15,'bold'),show="*",height=30,width=170,fg_color='transparent')
        repassword.place(x=440,y=310)

        signup_btn=customtkinter.CTkButton(self.name,text="Sign up",font=('vendana',15),command=sign_up,height=40,width=250)
        signup_btn.place(x=370,y=400)

        self.name.mainloop()

if __name__=="__main__":

    signup()
