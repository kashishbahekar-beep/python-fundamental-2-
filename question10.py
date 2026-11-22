#let create a number gusseing game .given a secret number (already decided by the user).write a program that asks the user 
#to guess it and print it 
#"To high" if the guess is above the number 
#to low ,if the guess is below 
#"coreect " if the guess match
secret_number = 7 
while True:
    guessing_number = int(input("enter a number:"))
    if guessing_number < secret_number:
        print("To high")
    elif guessing_number > secret_number:
        print("To low")
    else:
        print("correct!") 
        break       