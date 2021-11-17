"""
5. Write a script to convert decimal to hexadecimal

        Sample decimal number: 30, 4

        Expected output: 1e, 04
"""
while True:
    try:
        d = int(input("enter a decimal number: "))
        print("{0:02x}".format(d))

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)
        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")