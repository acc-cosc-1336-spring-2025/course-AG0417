import lists

exit = False

def check_exit():
    print("Are you sure you want to exit y/n")
    should_exit = input()
    if (should_exit == "y" or should_exit == "Y"):
        return True
    elif (should_exit == "n" or should_exit == "N"):
        return False

while exit == False:
    print("Homework 5 Menu\n1-List low/high values\n2-Exit")

    menu = int(input())
    list = []
    if menu == 1:
        while True:
            print("\nEnter a list value (list size 3 minimum)")
            # assuming the input is a valid int
            num = int(input())
            list.append(num)
            if list.__len__() >= 3:
                print("\nDo you want to enter another value? y/n")
                another = input()
                if (another == "n" or another == "N"):
                    break
        lowest = lists.get_lowest_list_value(list)
        highest = lists.get_highest_list_value(list)
        # make the prints far apart so easy to see hence the multiple newline characters
        print("\n\n\n\n\nLowest: " + str(lowest) + "\nHighest: " + str(highest) + "\n\n\n\n\n")
    elif menu == 2:
        exit = check_exit()