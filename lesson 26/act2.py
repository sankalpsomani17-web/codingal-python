import random
while True:
    num = random.randint(1,100)
    print("\nGuess a number between 1 and 100")
    for i in range(7):
        guess = int(input("guess: "))

        if guess == num:
            print(f"correct! you guessed it in {i+1} tries")
            break
        elif guess < num:
            print("too low")
        else:
            print("too high")
    else:
        print("you lost! the number was",num)

    if input("play again?(y/n) : ").lower() !='y':
        break