"""
3. Write a script to sum of the first n positive integers.
"""
while True:
    try:
        n = int(input("Input an integer: "))
        if n > 0:
            result = sum(range(n + 1))
            print("Sum of the first", n, "positive integers:", result)
        else:
            continue

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
