import repetition

exit = False

def check_exit():
    print("Are you sure you want to exit y/n")
    should_exit = input()
    if (should_exit == "y" or should_exit == "Y"):
        return True
    elif (should_exit == "n" or should_exit == "N"):
        return False

while exit == False:
    print("Homework 3 Menu\n1-Factorial\n2-Sum odd numbers\n3-Exit")

    menu = int(input())

    if menu == 1:
        print("What number do you want to find the factorial of?")
        num = int(input())
        while True:
            if (num > 0 and num < 10):
                break
            print("Invalid number")
        print(repetition.get_factorial(num))
    elif menu == 2:
        print("What number would you like the odd sum of?")
        num = int(input())
        while True:
            if (num > 0 and num < 100):
                break
            print("Invalid number")
        print(repetition.sum_odd_numbers(num))
    elif menu == 3:
        exit = check_exit()