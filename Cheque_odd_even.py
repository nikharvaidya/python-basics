#A program to cheque that number is off or even 
def cheque_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")   

number = int(input("Enter a number: "))
cheque_odd_even(number)

