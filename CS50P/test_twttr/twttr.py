def main():
    user_input = input("Input: ")
    msg = shorten(user_input)
    print("Output: " + msg)

def shorten(word):
    input_no_vowels = ""

    for i in word:
        if not i.lower() in ['a', 'e','i','o','u']:
            input_no_vowels += i

    return input_no_vowels


if __name__ == "__main__":
    main()

