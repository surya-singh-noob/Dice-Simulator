import random

a = 1
b = 6

while True:
    print(random.randint(a, b))
    
    roll_again = input("Want To Roll Dice Again?\n If yes press 'y'\n")
    
    if roll_again == 'y':
        continue
    else:
        break