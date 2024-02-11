# fuel


while True:

    fuel = input("Fraction: ")

    try:

        num, denom = fuel.split("/")

        new_num = int(num)
        new_denom= int(denom)

        f = new_num / new_denom

        if f <= 1 :
            break

    except (ValueError, ZeroDivisionError):
        pass

p = int(f * 100)

if p <= 1:
    print("E")

elif p >= 99:
    print("F")

else :
    print(f"{p}%")

