import signup
import original
import cryptocode
from tkinter import ttk,Tk,messagebox

class login:

    def __init__(self,name="login"):

        self.name=name
        self.name=Tk()
        self.name.title(name)
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)
            
        def log_in():

            condition=False
            usernames = username.get()

            password.config(show="")
            passwords = password.get()
            password.config(show="*")

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

            if condition:
                self.name.destroy()    
                original.original_win("journal")

            else:
                messagebox.showinfo("","Please check your username or password")

            user_pass.close()

        def sign_up():

            self.name.destroy()
            signup.signup("sign up")
                        
        username_label=ttk.Label(self.name,text="Username:",font=('vendana',15,'bold'))
        username_label.place(x=330,y=230,height=30,width=170)

        username=ttk.Entry(self.name,font=('vendana',15))
        username.place(x=440,y=231,height=30,width=170)

        password_label=ttk.Label(self.name,text="Password:",font=('vendana',15,'bold'))
        password_label.place(x=330,y=280,height=30,width=170)

        password=ttk.Entry(self.name,font=('vendana',15,'bold'),show="*")
        password.place(x=440,y=279,height=30,width=170)

        login_btn=ttk.Button(self.name,text="Login",command=log_in)
        login_btn.place(x=420,y=320,height=35,width=110)

        add_label=ttk.Label(self.name,text="New user?",font=('vendana',15, 'bold'))
        add_label.place(x=370,y=365)

        signup_btn=ttk.Button(self.name,text="Sign up",command=sign_up)
        signup_btn.place(x=480,y=365,height=30,width=120)

        text_label=ttk.Label(self.name,font=('vendana',9))
        text_label.place(x=350,y=395)

        self.name.mainloop()

if __name__=="__main__":
    
    login("login")