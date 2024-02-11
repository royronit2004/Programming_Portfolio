# FACES

def main():
    my_Input = input("Input: ")
    my_Input = convert(my_Input)
    print(my_Input)


def convert(my_Input):
    my_Input = my_Input.replace(":)", "🙂")
    my_Input = my_Input.replace(":(", "🙁")
    return my_Input

main()

