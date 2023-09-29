import MAIN
from tkinter import ttk,Tk

class signup:

    def __init__(self,name="Sign up"):
        
        self.name=name
        self.name=Tk()
        self.name.title(name)
        self.name.geometry('300x250+200+200')
        self.name.resizable(False,False)

        def sign_up():

            user_name=username.get()
            pass_word=password.get()

            repassword.config(show="")
            re_pass_word=repassword.get()
            repassword.config(show="*")

            if pass_word==re_pass_word:
                text_label.config(text="")

                try:
                    file=open("usernames_passwords.txt",'a')

                except:
                    file=open("usernames_passwords.txt",'w')

                file.write(user_name + "," + pass_word+"\n")
                file.close()

                self.name.destroy()
                MAIN.login()

            else:
                text_label.config(text="check and re-enter the password correctly")

        username_label=ttk.Label(self.name,text="Username:",font=("vendana",10,'bold'))
        username_label.place(x=45,y=50,height=30,width=70)

        username=ttk.Entry(self.name,font=('vendana',10))
        username.place(x=120,y=56,height=20,width=120)

        password_label=ttk.Label(self.name,text="Password:",font=("vendana",10,'bold'))
        password_label.place(x=45,y=80,height=30,width=70)

        password=ttk.Entry(self.name,font=('vendana',10,'bold'))
        password.place(x=120,y=86,height=20,width=120)

        repassword_label=ttk.Label(self.name,text="Re-enter the Password:",font=("vendana",10,'bold'))
        repassword_label.place(x=10,y=115,height=30,width=150)

        repassword=ttk.Entry(self.name,font=('vendana',10,'bold'),show="*")
        repassword.place(x=160,y=120,height=20,width=130)

        signup_btn=ttk.Button(self.name,text="Sign up",command=sign_up)
        signup_btn.place(x=120,y=150,height=40,width=60)

        text_label=ttk.Label(self.name)
        text_label.place(x=40,y=200,height=20,width=250)

        self.name.mainloop()

if __name__=="__main__":

    signup("signup")