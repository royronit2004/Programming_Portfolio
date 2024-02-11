# fuel

def main():
    fraction = input("Fraction: ")
    frac_conv = convert(fraction)
    output = gauge(frac_conv)
    print(output)


def convert(fraction):
    while True:
        try:

            num, denom = fraction.split("/")

            new_num = int(num)
            new_denom= int(denom)

            f = new_num / new_denom

            if f <= 1 :
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else :
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
