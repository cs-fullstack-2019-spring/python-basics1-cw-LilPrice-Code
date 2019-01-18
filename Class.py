def main():
    #problem1()
    #problem2()
    #problem3()
    #problem4()



def problem1():
    start = "My name is "
    Myname = input("What is your name? ")
    print(start + Myname)

def problem2():
    extra = int(input("Enter your Extra Credit! "))
    if(extra < 5):
        print("Not enough Extra Credit")
    elif(extra > 20):
        print("Too Much Extra Credit")
    else:
        print(extra)

def problem3():
    password1 = input("Enter a Password. ")
    password2 = input("Re-enter Password. ")
    if(password1 == password2):
        print("Password is Set")
    else:
        print("Try Again")

def problem4():
    card1 = int(input("Enter a card: "))
    card2 = int(input("Enter another card: "))
    card3 = int(input("Enter another card: "))
    blackjack = card1 + card2 + card3
    if(blackjack == 21):
        print("BLACKJACK!!!")
    elif(blackjack > 21):
        print("BUST!!")
    elif(blackjack < 21):
        print("The total is", blackjack)
    else:
        print("ERROR")

if __name__ == '__main__':
    main()