import signup
import original
from tkinter import ttk,Tk

class login:

    def __init__(self,name="login"):

        self.name=name
        self.name=Tk()
        self.name.title(name)
        self.name.geometry('300x250+200+200')
        self.name.resizable(False,False)
            
        def log_in():

            condition=False
            usernames = username.get()

            password.config(show="")
            passwords = password.get()
            password.config(show="*")

            user_pass = open("usernames_passwords.txt",'r')
            lines=user_pass.readlines()

            for line in lines:
                line = line.strip()
                arr=list(line.split(","))
                user_name=arr[0]
                pass_word=arr[1]

                if usernames==user_name and passwords==pass_word:
                    condition=True
                    break

            if condition:
                self.name.destroy()    
                original.original_win("journal")

            else:
                text_label.config(text="Please check your username or password")

            user_pass.close()

        def sign_up():

            self.name.destroy()
            signup.signup("sign up")
                        
        username_label=ttk.Label(self.name,text="Username:",font=('vendana',10,'bold'))
        username_label.place(x=45,y=50,height=30,width=70)

        username=ttk.Entry(self.name,font=('vendana',10))
        username.place(x=120,y=56,height=20,width=120)

        password_label=ttk.Label(self.name,text="Password:",font=('vendana',10,'bold'))
        password_label.place(x=45,y=80,height=30,width=70)

        password=ttk.Entry(self.name,font=('vendana',10,'bold'),show="*")
        password.place(x=120,y=86,height=20,width=120)

        login_btn=ttk.Button(self.name,text="Login",command=log_in)
        login_btn.place(x=100,y=120,height=30,width=100)

        add_label=ttk.Label(self.name,text="New user?",font=('vendana',10, 'bold'))
        add_label.place(x=85,y=165)

        signup_btn=ttk.Button(self.name,text="Sign up",command=sign_up)
        signup_btn.place(x=160,y=165)

        text_label=ttk.Label(self.name,font=('vendana',9))
        text_label.place(x=30,y=195)

        self.name.mainloop()

if __name__=="__main__":
    
    login("window")