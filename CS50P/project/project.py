#final project cs50p

import sys
import csv


def main():
    correct_arg()

    data = []

    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("Cannot read CSV file")

    output = []
    for row in data:
        universe = select_universe(row["favourite character"])
        grade = select_grade(row["birth-date"])
        output.append({"name": row["name"], "universe": universe, "grade": grade})
    print(output)

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name","universe","grade"])
        writer.writerow({"name": "name", "universe": "universe", "grade": "grade"})
        for row in output:
            writer.writerow({"name": row["name"], "universe": row["universe"], "grade": row["grade"]})


def correct_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV file")



def select_universe(char):
    if char in ["Iron-Man", "Spider-Man","Wolverine","Doctor Doom","Black Widow","Doctor Strange","Captain America"]:
        return "Marvel Universe"
    elif char in ["Batman", "Superman","Lex Luthor","Constantine","Riddler","Scarecrow","Ra's al Ghul"]:
        return "DC Universe"
    else:
        return "Might Be In DC or Marvel or Other."



def select_grade(year):
    age = 2023 - int(year)
    grade = age - 5
    return "Grade: " + str(grade)


if __name__ == "__main__":
    main()