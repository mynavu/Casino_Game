import random
import time

def random_num():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    return a,b,c

cash = 500
def pull_lever():
    global cash
    print("Your current input is $" + str(cash))
    time.sleep(1)
    print("-$100")
    cash -= 100
    time.sleep(1)
    print("Pulling the lever...")
    a, b, c = random_num()
    time.sleep(1)
    print("You got:", a, b, c)
    time.sleep(1)
    if a == b == c:
        print("You won $700")
        cash += 700
        print("Total cash: $" + str(cash))
    else:
        print("Better luck next time")
        print("Total cash: $" + str(cash))
    return cash

def casino():
    player = input("Do you wish to pay $500 to play? (yes/no) ")
    if player != "no":
        pull_lever()
        while True:
            play_again = input("Do you want to play another round? (yes/no) ")
            if play_again != "no":
                pull_lever()
                if cash == 0:
                    transfer()
                    print("Goodbye")
                    break
            else:
                print("Goodbye")
                break
    else:
        print("Goodbye")

def transfer():
    print("You have no cash left")
    more = input("Would you want to transfer $500 more? (yes/no) ")
    if more != "no":
        print("You now have $500 in cash")
        casino()
    else:
        cash == 0

casino()






