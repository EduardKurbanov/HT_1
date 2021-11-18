"""
2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.

        Test Data :

        color_list_1 = set(["White", "Black", "Red"])

        color_list_2 = set(["Red", "Green"])

        Expected Output :

        {'Black', 'White'}
"""
while True:
    try:
        print("enter two sets to compare")
        color_list_1 = set(input('enter sets number 1 through ",": ').split(","))
        color_list_2 = set(input('enter sets number 2 through ",": ').split(","))
        print("you entered the first set - > {0}".format(color_list_1))
        print("you entered the second set - > {0}".format(color_list_2))
        color_difference = color_list_1.difference(color_list_2)
        print("difference -> ".format(color_difference))

        print("*"*57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")

