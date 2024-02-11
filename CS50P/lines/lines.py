import sys


def main():
    chk_cmdl_arg()

    try:
        b = open(sys.argv[1])
        lines = b.readlines()


    except FileNotFoundError:
        print("File does not exist")

    count_lines = 0
    for line in lines:
        if chkl(line) == False:
            count_lines += 1

    print(count_lines)


def chk_cmdl_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")


def chkl(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
