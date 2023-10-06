import random

while True:
    
    print("Enter rock or paper or scissor")
    select=["rock","paper","scissor"]
    Player_score=0
    Computer_score=0
    
    for i in range(10): 
        
        Player=input("Enter:")
        computer=random.choice(select)
        print(computer)
        
        if(Player==computer):
            continue
            
        elif(Player=='rock' and computer=='paper') or (Player=='paper' and computer=='scissor') or (Player=='scissor' and computer=='rock'):
            Computer_score+=1
            
        else:
            Player_score+=1
            
    print("player score:",Player_score)
    print("computer score:",Computer_score)
    
    if(Player_score>Computer_score):
        print("Player wins")
        
    elif(Player_score<Computer_score):
        print("Computer wins")
        
    else:
        print("DRAW")
        
    print("You wanna play again:(y/n):")
    option=input()
    
    if(option=='n'):
        print("Thank you for playing")
        break
