def grid_reset():
  global z,b,c,d,e,f,g,h,x
  z='a';b='b';c='c';d='d';e='e';f='f';g='g';h='h';x='i'

def grid(op,num):
  global z,b,c,d,e,f,g,h,x,stop_game

  if num==0:
    if op=='a' and z!="O" and z!="X":
      z="X"
    elif op=='b' and b!="O" and b!="X":
      b="X"
    elif op=='c' and c!="O" and c!="X":
      c="X"
    elif op=='d' and d!="O" and d!="X":
      d="X"
    elif op=='e' and e!="O" and e!="X":
      e="X"
    elif op=='f' and f!="O" and f!="X":
      f="X"
    elif op=='g' and g!="O" and g!="X":
      g="X"
    elif op=='h' and h!="O" and h!="X":
      h="X"
    elif op=='i' and x!="O" and x!="X":
      x="X"
    else:
      print(f"player {num+1} sorry, thats a invalid move and you lost your move \n better dont repeat next time")

    print("       |       |     ")
    print(f"   {z}   |   {b}   |   {c}  ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {d}   |   {e}   |   {f}  ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {g}   |   {h}   |   {x}  ")
    print("       |       |     ")

    if (z == 'X' and b == 'X' and c == 'X')or\
        (d == 'X' and e == 'X' and f == 'X')or\
        (g == 'X' and h == 'X' and x == 'X')or\
        (z == 'X' and d == 'X' and g == 'X')or\
        (b == 'X' and e == 'X' and h == 'X')or\
        (c == 'X' and f == 'X' and x == 'X')or\
        (z == 'X' and e == 'X' and x == 'X')or\
        (g == 'X' and e == 'X' and c == 'X'):
        print(f"player {num+1} wins")
        stop_game=False

  elif num==1:
    if op=='a' and z!="X" and z!="O":
      z="O"
    elif op=='b' and b!="X" and b!="O":
      b="O"
    elif op=='c' and c!="X" and c!="O":
      c="O"
    elif op=='d' and d!="X" and d!="O":
      d="O"
    elif op=='e' and e!="X" and e!="O":
      e="O"
    elif op=='f' and f!="X" and f!="O":
      f="O"
    elif op=='g' and g!="X" and g!="O":
      g="O"
    elif op=='h' and h!="X" and h!="O":
      h="O"
    elif op=='i' and x!="X" and x!="O":
      x="O"
    else:
      print(f"player {num+1} sorry, thats a invalid move and you lost your move \n better dont repeat next time")

    print("       |       |     ")
    print(f"   {z}   |   {b}   |   {c}  ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {d}   |   {e}   |   {f}  ")
    print("       |       |     ")
    print("----------------------")
    print("       |       |     ")
    print(f"   {g}   |   {h}   |   {x}  ")
    print("       |       |     ")

    if (z == 'O' and b == 'O' and c == 'O')or\
        (d == 'O' and e == 'O' and f == 'O')or\
        (g == 'O' and h == 'O' and x == 'O')or\
        (z == 'O' and d == 'O' and g == 'O')or\
        (b == 'O' and e == 'O' and h == 'O')or\
        (c == 'O' and f == 'O' and x == 'O')or\
        (z == 'O' and e == 'O' and x == 'O')or\
        (g == 'O' and e == 'O' and c == 'O'):
        print(f"player {num+1} wins")
        stop_game=False

z='a';b='b';c='c';d='d';e='e';f='f';g='g';h='h';x='i'
stop_game=True

print("       |       |     ")
print(f"   {z}   |   {b}   |   {c}  ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print(f"   {d}   |   {e}   |   {f}  ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print(f"   {g}   |   {h}   |   {x}  ")
print("       |       |     ")

while True:

  if stop_game==False:
    break

  if i%9==0:
    print("Out of chances")
    choice=input("you wanna play again?(y/n):")

    if choice=="y":
      i=0
      grid_reset()

    else:
      break

  move=input(f"player {(i%2)+1}:")
  
  if move=="exit":
    break

  grid(move,i%2)