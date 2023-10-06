from msilib.schema import SelfReg
import random
from tkinter import ttk,Tk,Text,END

class rock_paper_scissor:
    
    def __init__(self,name="rock paper scissor"):

        self.name=name
        self.root=Tk()
        self.root.geometry("410x340+100+100")
        self.root.resizable(False,False)

        self.computer_choice=["rock","paper","scissor"]
        self.choice=random.choice(self.computer_choice)

        self.computer_score=0
        self.player_score=0

        def rock():
            text.config(state='normal') 
            self.choice=random.choice(self.computer_choice)
            text.delete("1.0","end-1c")
            text.insert(END,"Rock\n")
            if(self.choice=="rock"):
                message="Computer chose same, so draw"
            elif self.choice=="paper":
                message="Computer chose paper"
                self.computer_score+=1
            else:
                message="computer chose scissor"
                self.player_score+=1
            text.insert(END,f"{message}") 
            text.insert(END,f"\nplayer score:{self.player_score}")  
            text.insert(END,f"\nComputer score:{self.computer_score}")  
            text.config(state='disabled')   

        def paper():
            text.config(state='normal') 
            self.choice=random.choice(self.computer_choice)
            text.delete("1.0","end-1c")
            text.insert(END,"Paper\n")
            if(self.choice=="paper"):
                message="Computer chose same, so draw"
            elif self.choice=="scissor":
                message="Computer chose scissor"
                self.computer_score+=1
            else:
                message="Computer chose rock"
                self.player_score+=1
            text.insert(END,f"{message}") 
            text.insert(END,f"\nPlayer score:{self.player_score}") 
            text.insert(END,f"\nComputer score:{self.computer_score}")  
            text.config(state='disabled')  

        def scissor():
            text.config(state='normal') 
            self.choice=random.choice(self.computer_choice)
            text.delete("1.0","end-1c")
            text.insert(END,"Scissor\n")
            if(self.choice=="scissor"):
                message="Computer chose same, so draw"
            elif self.choice=="rock":
                message="Computer chose rock"
                self.computer_score+=1
            else:
                message="Computer chose paper"
                self.player_score+=1
            text.insert(END,f"{message}") 
            text.insert(END,f"\nPlayer score:{self.player_score}") 
            text.insert(END,f"\nComputer score:{self.computer_score}")  
            text.config(state='disabled') 

        def new():
            text.config(state='normal') 
            self.computer_score=0
            self.player_score=0
            text.delete("1.0","end-1c")    
            text.insert(END,f"Player score:{self.player_score}\n")
            text.insert(END,f"Computer score:{self.computer_score}\n")
            text.config(state='disabled') 

        def end():
            text.config(state='normal') 
            text.delete("1.0","end-1c")    
            text.insert(END,f"player score:{self.player_score}\n")
            text.insert(END,f"computer score:{self.computer_score}\n")
            if self.player_score>self.computer_score:
                message=f"Congrats! Player wins with {self.player_score-self.computer_score} points"   
            elif self.player_score<self.computer_score:
                message=f"Computer wins with {self.computer_score-self.player_score} points\n better luck next time"
            elif self.player_score==self.computer_score:
                message=f"Draw, player and computer has equal {self.player_score} points " 
            text.insert(END,f"{message}")
            text.config(state='disabled') 

        rock_button=ttk.Button(self.root,text="rock",padding=10,width=18,command=rock)
        rock_button.grid(row=1,column=1)

        paper_button=ttk.Button(self.root,text="paper",padding=10,width=18,command=paper)
        paper_button.grid(row=1,column=2)

        scissor_button=ttk.Button(self.root,text="scissor",padding=10,width=18,command=scissor)
        scissor_button.grid(row=1,column=3)

        text=Text(self.root,width=30,height=10,font=("Verdana",15))
        text.grid(row=2,column=1,columnspan=3)

        new_game_button=ttk.Button(self.root,text="new game",padding=10,width=18,command=new)
        new_game_button.grid(row=3,column=1)

        end_button=ttk.Button(self.root,text="end",padding=10,width=18,command=end)
        end_button.grid(row=3,column=3)

        self.root.mainloop()

if __name__=="__main__":

    rock_paper_scissor()