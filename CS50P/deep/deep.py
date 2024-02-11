# DEEP THOUGHT


def main():
    # Prompt the user for input
    user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Convert the input to lowercase and remove any spaces
    user_input = user_input.lower().replace(" ", "")

    # Now Check if the input matches any of the accepted answers
    if user_input == "42" or user_input == "fortytwo" or user_input == "forty-two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()