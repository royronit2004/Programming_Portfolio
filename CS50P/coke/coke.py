# coke

coke_due = 50


while coke_due > 0 :
    print("Amount Due:", coke_due)

    coin_given = int(input("Insert Coin:"))

    if coin_given in [25, 10 ,5]:
        coke_due -= coin_given


change_owed = abs(coke_due)

print("Change Owed:", change_owed)

