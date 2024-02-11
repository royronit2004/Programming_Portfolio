# figlet

from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    is_random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    is_random = False
else:
    sys.exit[1]


figlet.getFonts()

if is_random == False:
    try:

        figlet.setFont(font=sys.argv[2])

    except:
        print("Invalid")
        sys.exit[1]

else:
    font = random.choice(figlet.getFonts())



user_input = input("Input: ")

print("Output: ")
print(figlet.renderText(user_input))

