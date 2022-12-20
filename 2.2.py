import random

dice = random.randint(1, 6)
prize_dice = random.randint(1, 6)

while True:
    if dice != 6:
        print("dice number =", dice)
        break
    elif dice == 6:
        print("dice number =", dice)
        print("you can re-roll the dice😀")
        print("dice number =", prize_dice)
        break
