# outdated

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = (input("Date: "))

    try:

        month, day, year = user_input.split("/")

        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break

    except:
        try:
            new_month, new_day, year = user_input.split(" ")

            for m in range(len(months)):
                if new_month == months[m]:
                    month = m + 1


            day = new_day.replace(",","")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break

        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")
