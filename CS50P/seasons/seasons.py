from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():

    birth_day = input("Date of Birth: ")

    try:
        year, month, day = check_bd(birth_day)
    except:
        sys.exit("Invalid Date")
    d_o_b = date(int(year), int(month), int(day))
    d_o_t = date.today()
    diff = d_o_t - d_o_b
    tot_min = diff.days * 24 * 60
    output = p.number_to_words(tot_min, andword="")
    print(output.capitalize() + " minutes")


def check_bd(birth_day):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_day):
        year, month, day = birth_day.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
