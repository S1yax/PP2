
import random
def game():
    print("Hello! What is your name?")
    a=input()
    print("Well,",a,", I am thinking of a number between 1 and 20.")
    import random
    number= random.randint(1, 20)
    att= 0
    while True:
        guess = int(input("Take a guesS"))
        att=+1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Good job,",a,f"! You guessed my number in {att}  guesses!")
            break
game()