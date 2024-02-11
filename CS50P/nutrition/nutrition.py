# nutrition


fruit = {

    "apple": 130,
    "banana": 110,
    "avocado": 50,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 6,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80

}

fruit_name = input("Item: ")

for key in fruit:
    if key == fruit_name.lower():
        print("Calories:", fruit[key])


