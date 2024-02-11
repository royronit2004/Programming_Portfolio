#MATH INTERPRETER

def calculate(x, y, z):
    x, z = float(x), float(z)
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    elif y == '/':
        return x / z
    else:
        return("Invalid")


def main():
    expression = input("Expression: ")

    x, y, z = expression.split()

    result = calculate(x, y, z)

    result = calculate(x, y, z)
    formatted_result = "{:.1f}".format(result)

    print("Answer: ", formatted_result)

if __name__ == "__main__":
    main()
    