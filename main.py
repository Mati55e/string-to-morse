from morse_code import dictionary


def str_to_morse(user_string):
    new_string = ""
    for position in range(len(user_string)):
        if user_string[position] in dictionary:
            new_string += dictionary[user_string[position]] + " "
        else:
            new_string += user_string[position] + " "
    return new_string


one_more = True
while one_more:
    # Get user input
    user_input = input("Write you message: ").lower()
    # Convert user input to string and print
    print(str_to_morse(user_input))
    # Try again loop
    wrong_input = True
    while wrong_input:
        user_want_more = input("Do you want more? Y or N?").lower()
        if user_want_more == "y":
            one_more = True
            wrong_input = False
        elif user_want_more == "n":
            one_more = False
            wrong_input = False
        else:
            wrong_input = True
