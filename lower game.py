import random
import time

def results(tries, winnum, ai_tries):
    """This function prints the results if they guessed the right number and asks if they want to play again"""
    print(f"You got it in {tries} tries!")
    print(f"The ai got it in {ai_tries} tries!")
    print(f"The number was {winnum}")
    if tries > ai_tries:
        print("The ai won.")
    elif tries < ai_tries:
        print("You won!")
    while True:
        play_again = input("Would you like to play again, yes or no: ")
        if play_again == "y" or play_again == "yes":
            main()
        elif play_again == "n" or play_again == "no":
            print("Have a good day")
            break
        else:
            print("Please put either y, yes, n, or no.")

def pick_num(winnum, low, high):
    """This function makes the user pick the number and if its the winning number it will print the results, if not it will ask again"""
    tries = 0
    while True:
        try:
            choice = int(input("Pick a number 0 - 100: "))
        except:
            print("Invalid input")
            continue
        #make sure num is in range
        if choice > 100 or choice < 1:
            print("Number should be in between 0-100")
            continue
        tries += 1
        if choice > winnum:
            print(f"Winning number is less than {choice}.")
        elif choice < winnum:
            print(f"Winning number is more than {choice}.")
        else:
            ai_pick_number(tries, winnum, low, high)
            break

def ai_pick_number(tries, winnum, low, high):
    """This function has the ai pick a number using binary logic until it guesses the correct number"""
    ai_tries = 0
    while True:
        time.sleep(1)
        ai_tries += 1
        middle = (low + high) / 2
        middle = round(middle)
        print(f"Ai chose {middle}")
        if middle > winnum:
            print(f"Winning number is less than {middle}.")
            high = middle
        elif middle < winnum:
            print(f"Winning number is more than {middle}.")
            low = middle
        elif winnum == middle:
            results(tries, winnum, ai_tries)
            break
        
def main():
    low = 0
    high = 100
    winning_number = random.randint(0,100)
    pick_num(winning_number, low, high)    

if __name__ == "__main__":
    main()