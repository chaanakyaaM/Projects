import cryptocode

class encrypt_and_decrypt:

    def __init__(self):

        key=input("Enter your key:")
        msg=input("Enter your message:")
        mode=input("you wanna encode or decode:")

        if mode == "encode":
            main_msg=cryptocode.encrypt(msg,key)
            print(main_msg)
            
        else:
            main_msg=cryptocode.decrypt(msg,key)
            print(main_msg)

if __name__=="__main__":

    encrypt_and_decrypt()







