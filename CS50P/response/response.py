from validator_collection import validators


def main():

    email = input("What's your email address? ")

    try:
        email_Valid = validators.email(email)

        print("Valid")

    except:
        print("Invalid")


if __name__ == "__main__":
    main()