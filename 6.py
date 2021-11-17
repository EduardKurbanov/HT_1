"""
6. Write a script to check whether a specified value is contained in a group of values.

        Test Data :

        3 -> [1, 5, 8, 3] : True

        -1 -> (1, 5, 8, 3) : False
"""
while True:
    try:
        enter_mas = list(input("input list: ").split(","))
        list_1 = []
        for i in enter_mas:
            list_1.append(int(i))
        print(list_1)
        check = int(input("enter a value to check: "))
        print("{0} -> {1} : {2}".format(check, list_1, check in list_1))

        enter_mas = list(input("input tuple: ").split(","))
        list_1 = []
        for i in enter_mas:
            list_1.append(int(i))
        print(tuple(list_1))
        check = int(input("enter a value to check: "))
        print("{0} -> {1} : {2}".format(check, list_1, check in list_1))

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")

