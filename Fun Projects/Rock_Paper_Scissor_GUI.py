import random
import random
from tkinter import ttk
from tkinter import *

root=Tk()
root.title("rock paper scissor")
root.geometry("410x340+100+100")

computer_choice=["rock","paper","scissor"]
choice=random.choice(computer_choice)
print(choice)


computer_score=0
player_score=0


def rock():
    global computer_score
    global player_score
    global choice
    choice=random.choice(computer_choice)
    text.delete("1.0","end-1c")
    text.insert(END,"Rock\n")
    if(choice=="rock"):
        message="Computer chose same, so draw"
    elif choice=="paper":
        message="Computer chose paper"
        computer_score+=1
    else:
        message="computer chose scissor"
        player_score+=1
    text.insert(END,f"{message}") 
    text.insert(END,f"\nplayer score:{player_score}")  
    text.insert(END,f"\nComputer score:{computer_score}")    

def paper():
    global computer_score
    global player_score
    global choice
    choice=random.choice(computer_choice)
    text.delete("1.0","end-1c")
    text.insert(END,"Paper\n")
    if(choice=="paper"):
        message="Computer chose same, so draw"
    elif choice=="scissor":
        message="Computer chose scissor"
        computer_score+=1
    else:
        message="Computer chose rock"
        player_score+=1
    text.insert(END,f"{message}") 
    text.insert(END,f"\nPlayer score:{player_score}") 
    text.insert(END,f"\nComputer score:{computer_score}")    

def scissor():
    global computer_score
    global player_score
    global choice
    choice=random.choice(computer_choice)
    text.delete("1.0","end-1c")
    text.insert(END,"Scissor\n")
    if(choice=="scissor"):
        message="Computer chose same, so draw"
    elif choice=="rock":
        message="Computer chose rock"
        computer_score+=1
    else:
        message="Computer chose paper"
        player_score+=1
    text.insert(END,f"{message}") 
    text.insert(END,f"\nPlayer score:{player_score}") 
    text.insert(END,f"\nComputer score:{computer_score}")  

def new():
    global computer_score
    global player_score
    computer_score=0
    player_score=0
    text.delete("1.0","end-1c")    
    text.insert(END,f"Player score:{player_score}\n")
    text.insert(END,f"Computer score:{computer_score}\n")

def end():
    global computer_score
    global player_score
    text.delete("1.0","end-1c")    
    text.insert(END,f"player score:{player_score}\n")
    text.insert(END,f"computer score:{computer_score}\n")
    if player_score>computer_score:
        message=f"Congrats! Player wins with {player_score-computer_score} points"   
    elif player_score<computer_score:
        message=f"Computer wins with {computer_score-player_score} points\n better luck next time"
    elif player_score==computer_score:
        message=f"Draw, player and computer has equal {player_score} points " 
    text.insert(END,f"{message}")

rock_button=ttk.Button(root,text="rock",padding=10,width=18,command=rock)
rock_button.grid(row=1,column=1)

paper_button=ttk.Button(root,text="paper",padding=10,width=18,command=paper)
paper_button.grid(row=1,column=2)

scissor_button=ttk.Button(root,text="scissor",padding=10,width=18,command=scissor)
scissor_button.grid(row=1,column=3)

text=Text(root,width=30,height=10,font=("Verdana",15))
text.grid(row=2,column=1,columnspan=3)

new_game_button=ttk.Button(root,text="new game",padding=10,width=18,command=new)
new_game_button.grid(row=3,column=1)

end_button=ttk.Button(root,text="end",padding=10,width=18,command=end)
end_button.grid(row=3,column=3)


root.mainloop()