import random
num=random.randint(1,10)
guess=int(input("Guess A No 1 To 10:"))
a=1
while num!=guess:
    a=a+1    
    if guess<num:
        print("Guess Higher")
        guess=int(input("Enter A no"))
        
    elif guess>num:        
        print("Guess Lower")
        guess=int(input("Enter A no"))                  
if num==guess:
    print("You Gussed The Correct No In",a,"No Of Tries")