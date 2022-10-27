import random
def guessing_game(target):
    counter = 0
    while True:
        while counter < 3:
            user = int(input("enter a guess from 1-9: "))
            if user == target:
                return print("CONGRATS YOU ARE RIGHT!")
            elif user < target:
                print("You guessed too low")
            elif user > target:
                print("you guessed to high")
            counter +=1 
        return print(("Game Over Sorry :("))

        

def main():
    target = random.randint(1,10)
    guessing_game(target)

main()














