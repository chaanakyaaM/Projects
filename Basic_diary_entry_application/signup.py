import MAIN
from tkinter import ttk,Tk,messagebox
import cryptocode

class signup:

    def __init__(self,name="Sign up"):
        
        self.name=name
        self.name=Tk()
        self.name.title(name)
        self.name.geometry("1000x700+250+50")
        self.name.resizable(False,False)

        def sign_up():

            user_name=username.get()
            pass_word=password.get()

            encrypted_username=cryptocode.encrypt(user_name,pass_word)

            encrypted_password=cryptocode.encrypt(pass_word,user_name)
            print(encrypted_password)
            print(encrypted_username)


            #username
            #password

            repassword.config(show="")
            re_pass_word=repassword.get()
            repassword.config(show="*")

            if pass_word==re_pass_word:
                text_label.config(text="")

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

        username_label=ttk.Label(self.name,text="Username:",font=("vendana",15,'bold'))
        username_label.place(x=330,y=230,height=30,width=110)

        username=ttk.Entry(self.name,font=('vendana',15))
        username.place(x=440,y=231,height=30,width=170)

        password_label=ttk.Label(self.name,text="Password:",font=("vendana",15,'bold'))
        password_label.place(x=330,y=270,height=30,width=110)

        password=ttk.Entry(self.name,font=('vendana',15,'bold'))
        password.place(x=440,y=270,height=30,width=170)

        repassword_label=ttk.Label(self.name,text="Re-enter the Password:",font=("vendana",15,'bold'))
        repassword_label.place(x=280,y=315,height=30,width=230)

        repassword=ttk.Entry(self.name,font=('vendana',15,'bold'),show="*")
        repassword.place(x=510,y=310,height=30,width=170)

        signup_btn=ttk.Button(self.name,text="Sign up",command=sign_up)
        signup_btn.place(x=420,y=350,height=40,width=100)

        text_label=ttk.Label(self.name)
        text_label.place(x=340,y=400,height=20,width=250)

        self.name.mainloop()

if __name__=="__main__":

    signup()
