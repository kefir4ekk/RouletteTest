import random

start_num = int(input("Enter start number - "))
end_num = int(input("Enter end number - "))
print("Succesfuly")

while True:
    guess = int(input('Enter Number - '))
    guess1 = random.randint(start_numb, end_numb)

    if guess == guess1:
        print("You won!")
        print("The number was - ", guess1)
        b = input("Exit? - ")
        if b == 'Yes':
            print("Exit")
            break
        continue

    else:
        print("You lose!")
        print("The number was - ", guess1)
        print("Try again")
        b = input("Exit? - ")
        if b == 'Yes':
            print("Exit")
            break
        continue