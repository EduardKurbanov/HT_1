"""
.Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

        Sample data : 1, 5, 7, 23

        Output :

        List : [‘1', ' 5', ' 7', ' 23']

        Tuple : (‘1', ' 5', ' 7', ' 23')
"""
while True:
    try:
        enter_mas = list(input("input numbers: ").split(","))
        print(enter_mas)
        tuple_mas = tuple(enter_mas)
        print(tuple_mas)

        print("*"*57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
