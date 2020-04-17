def safe_input(number, functype='port'):
    if functype == 'loop_back':
        while not number.isdigit() or int(number) < 0 or int(number) > 1:
            number = input("Enter number once again:")
    else:
        while not number.isdigit() or int(number) < 0:
            number = input("Enter number once again: ")
    return int(number)
