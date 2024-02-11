# HOME FEDERAL SAVINGS

def main():
    # Prompt the user for input and strip leading whitespace
    user_input = input("Please enter a greeting: ").lstrip()

    # Convert the input to lowercase
    user_input = user_input.lower()

    # Check the conditions and output the corresponding amount
    if user_input.startswith("hello"):
        print("$0")
    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
