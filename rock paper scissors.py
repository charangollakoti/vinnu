print(f"Enter r for rocks\nEnter p for papers\nEnter s for scissors")
firstplayer = input("Enter Player1 choice : ")
secondplayer = input("Enter Player2 choice : ")
if len(firstplayer) > 1 or len(firstplayer) <= 0 or len(secondplayer) > 1 or len(secondplayer) <= 0:
    print("Invalid inputs Please try again")
else:
    if firstplayer == "r" and secondplayer == "p":
        print("Player2 wins!!")
    elif firstplayer == "r"  and secondplayer == "s":
        print("Player1 wins!!")
    elif firstplayer == "p" and secondplayer == "r":
        print("Player1 wins!!")
    elif firstplayer == "p" and secondplayer == "s":
        print("Player2 wins!!")
    elif firstplayer == "s" and secondplayer == "r":
        print("Player2 wins!!")
    elif firstplayer == "s" and secondplayer == "p":
        print("Player1 wins!!")
    else:
        print("Its a tie!!")
