import signup
import original
import cryptocode
import customtkinter
from tkinter import ttk,Tk,messagebox


class login:

    def __init__(self,name="login"):

        self.name=name
        self.name=customtkinter.CTk()
        self.name.title(name)
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)
            
        def log_in():

            condition=False
            usernames = username.get()

            password.configure(show="")
            passwords = password.get()
            password.configure(show="*")

            try:
                user_pass = open("encrypted_usernames_passwords.txt",'r')
                lines = user_pass.readlines()
            

                for line in lines:
                    line = line.strip()
                    arr=list(line.split(","))

                    user_name = arr[0]
                    pass_word = arr[1]

                    decrypted_username = cryptocode.decrypt(user_name,passwords)
                    decrypted_password = cryptocode.decrypt(pass_word,usernames)

                    if usernames==decrypted_username and passwords==decrypted_password:
                        condition=True
                        break
            except:
                messagebox.showinfo("info","No Usernames are registured, try signing up")

            if condition:
                self.name.destroy()    
                original.original_win("journal")

            else:
                messagebox.showinfo("","Please check your username or password")

            user_pass.close()

        def sign_up():

            self.name.destroy()
            signup.signup("sign up")
            
        div_area=customtkinter.CTkTextbox(self.name,state='disabled',height=200,width=500,corner_radius=10,border_color='white',border_width=1,fg_color='black')
        div_area.place(x=240,y=180)

        username_label=customtkinter.CTkLabel(self.name,text="Username:",font=("vendana",15,'bold'),height=30,width=110,fg_color='black')
        username_label.place(x=330,y=230)

        username=customtkinter.CTkEntry(self.name,font=('vendana',15),height=30,width=170,fg_color='transparent')
        username.place(x=440,y=231)

        password_label=customtkinter.CTkLabel(self.name,text="Password:",font=("vendana",15,'bold'),height=30,width=110,fg_color='black')
        password_label.place(x=330,y=270)

        password=customtkinter.CTkEntry(self.name,font=('vendana',15,'bold'),show="*",height=30,width=170,fg_color='transparent')
        password.place(x=440,y=270)

        login_btn=customtkinter.CTkButton(self.name,text="Login",font=('vendana',15),command=log_in,height=35,width=200)
        login_btn.place(x=380,y=320)

        signup_label=customtkinter.CTkLabel(self.name,text="New User?",font=('vendana',15),height=40,width=150)
        signup_label.place(x=320,y=400)

        signup_btn=customtkinter.CTkButton(self.name,text="Sign up",font=('vendana',15),command=sign_up,height=35,width=200)
        signup_btn.place(x=450,y=400)

        self.name.mainloop()

if __name__=="__main__":
    
    login("login")