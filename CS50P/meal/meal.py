#MEAL

def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))

    # Convert the time to the corresponding number of hours as a float
    return hours + minutes / 60

def main():
    # Prompt the user for input (time)
    time_str = input("Enter Time in 24 Hour Format (e.g., 08:30): ")

    # Convert the time string to the corresponding number of hours
    time_in_hours = convert(time_str)

    # Check the time and output the corresponding meal
    if 6 <= time_in_hours < 12:
        print("breakfast time")
    elif 12 <= time_in_hours < 14:
        print("lunch time")
    elif 18 <= time_in_hours < 21:
        print("dinner time")
    else:
        print("Snacks Time!")

if __name__ == "__main__":
    main()

