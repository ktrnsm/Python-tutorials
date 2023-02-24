numb=25
turn=10

while turn>0:
    quess=int(input("please  write a number"))
    if quess<0:
        print("please advise a possitive number")
        continue
    turn-=1
    if numb==quess:
        print("huhu thats correct")
        break
    elif numb>quess:
        print("bigger number you have only {} turn".format(turn))
    else:
        print("lower number you have only{} turn to quees correct".format(turn))
    if turn==0:
        print("you have no turn left the corect number was {}".format(numb))