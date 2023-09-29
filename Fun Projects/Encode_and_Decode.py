import cryptocode

key=input("Enter your key:")
msg=input("Enter your message:")
mode=input("you wanna encode or decode:")
if mode == "encode":
    endoe=cryptocode.encrypt(msg,key)
    print(endoe)
else:
    enode=cryptocode.decrypt(msg,key)
    print(enode)



