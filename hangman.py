import random

my_list=['tiger','nande','sugoi','yamete']

my_list = random.choice(my_list)
turns = 10
guesses=''

while turns > 0:
    print(f"You have{turns} turns left")
    guessed_all=True

    for c in my_list:
        if c in guesses:
            print(c, end=' ')
        else:
            print('_',end=' ')
            guessed_all= False
    print()
    

    if not guessed_all:
        guess= input("Guess a char:")
        guesses = guesses + guess
        if guess not in my_list:
            turns = turns - 1
    else:
     turns = 0