import tkinter as tk
from tkinter import *
from tkinter import ttk
import cryptocode

root = tk.Tk()
root.title("Encrypt and Decrypt Messages")
root = tk.Frame(root)
 
key_label=ttk.Label(root,text="Enter your Key:-",padding=3)
key_label.pack()

key_entry=ttk.Entry(root,width=50)
key_entry.pack()

message_label=ttk.Label(root,text="Enter your Message:-",padding=3)
message_label.pack()

message_entry=ttk.Entry(root,width=50)
message_entry.pack()

def encrypt():
    output_label.delete(0,END)
    output_label.pack()
    msg1=cryptocode.encrypt(message_entry.get(),key_entry.get())
    output_label.insert(0,msg1)
    output_label.state(['readonly'])
    output_label.state(['!readonly'])
    output_label.pack()

def decrypt():
    output_label.delete(0,END)
    output_label.pack()
    msg1=cryptocode.decrypt(message_entry.get(),key_entry.get())
    output_label.insert(0,msg1)
    output_label.state(['readonly'])
    output_label.state(['!readonly'])
    output_label.pack()

encrypt_button=ttk.Button(root,text="Encrypt",command=encrypt,padding=2)
encrypt_button.pack()

decrypt_button=ttk.Button(root,text="Decrypt",command=decrypt)
decrypt_button.pack()

output_label=ttk.Entry(root,width=100)
output_label.pack()

root.pack()
root.mainloop()