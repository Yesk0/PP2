from random import randint




def game(x):
    name = input("Hello! What is your name?")
    step = 0
    txt = "Good job, KBTU! You guessed my number in {} guesses!"
    txt2 = "Your guess is too low."
    txt3 = "Your guess is too high."
    txt4 = "Take a guess."
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    y = int(input())
    while True:
        step += 1
        if y == x:
            print(txt.format(step))
            break
        elif y < x:
            print(txt2)
            print(txt4)
            y = int(input())
            continue
        elif y > x:
            print(txt3)
            print(txt4)
            y = int(input())
            continue  
        

x = randint(1, 20)
game(x)
