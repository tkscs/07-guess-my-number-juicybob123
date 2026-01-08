# the user will choose a number
# this program will guess the number
# the user will say "yes" or "higher" or "lower"
# the program will ask to play again or exit
x = 1
guess_number = 0
import random
y = 500000
z =  100000
number1 = 1
number2 = 500000
number3 = 1000000
number = random.randint(1,1000000)
d = 0

wg = int(input("write 1 if you want to guess write 2 if you want the computer to guess"))
if wg == 1:
    while x > 0.5:
        guess = int(input("input a number between 1, 1,000,000 "))

        if guess > 1000000:  
            print("please pick a number between 1 and 1,000,000 ")
        elif guess < 1:
            print("please pick a number between 1 and 1,000,000" )

        elif guess > number:
            print("less ")
            guess_number = guess_number + 1
        elif guess < number:
            print("more ")
            guess_number = guess_number + 1
        elif number == guess:
            print("you win ")
            x = 0
            print(f"you won in {guess_number} ")
if wg == 2:
    while x > 0.5:
        500000
        print(random.randint(number1,number2))
        mol= int(input("write 1 if its less and 2 if its more then your number 3 if its correct"))
        if mol == 1:
            
        elif mol == 2:
    
            number2 = int(number2 * random.uniform(1,2))
            number2 // 1
            print(number2)
    
        elif mol == 3:
            print(f"i won")
            x = 0
        else:
            print("chose 1 2 or 3 please")

        # if mol == 1:
        #     number1 == y
        #     y = random.randomint(number1,number2)
        #     print(y)
            
        # if mol == 2:

        #     z = random.randomint(number2,number3)
        #     print(z)




            

#8123