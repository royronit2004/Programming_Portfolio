# vanity plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(v):
    if len(v) > 6 or len(v) < 2:
        return False

    if v[0].isalpha() == False or v[1].isalpha() == False:
        return False

    i = 0
    while i < len(v):
        if v[i].isalpha() == False:
            if v[i] == '0':
                return False
            else:
                break

        i += 1

    for c in v:
        if c in ['.', ' ', '!', '?']:
            return False

    return True


main()
