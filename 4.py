"""
4. Write a script to concatenate N strings.
"""

while True:
    try:
        enter_num = int(input("enter a number to enter the number of lines: "))
        sent_str = ""
        for i in range(1, enter_num + 1):
            enter_str = input(str(i) + ". venter the string: ")
            sent_str += enter_str

            if i == enter_num:
                exit_str = input("enter an empty string to sum the lines: ")
                break
        print("string concatenation -> " + sent_str)

        print("*" * 57)
        yes = input('if you want to leave the program press "Y" if not then "N": ')
        print("*" * 57)

        if "y" == yes.lower():
            break
        else:
            continue
    except:
        print("error")
