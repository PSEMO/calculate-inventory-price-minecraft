sum = 0

def calculateWorth(itemName, itemPrice, ammount):
    print("You have " + ammount + " ammount of \"" + itemName + "\"")
    itemAmmount = ammount

    worth = itemAmmount * itemPrice
    print(worth)
    return worth

def calculateWorth(itemName, itemPrice):
    print("Enter the ammount of \"" + itemName + "\" you have.")
    itemAmmount = int(input("Enter an integer: "))

    worth = itemAmmount * itemPrice
    print(worth)
    return worth

sum = sum + calculateWorth("coal", 2)
sum = sum + calculateWorth("diamond", 75)
sum = sum + calculateWorth("emerald", 30)
sum = sum + calculateWorth("gold", 50)
sum = sum + calculateWorth("iron", 20)
sum = sum + calculateWorth("lapis lazuli", 5)
sum = sum + calculateWorth("redstone", 3)
sum = sum + calculateWorth("cobblestone", 0.3)
sum = sum + calculateWorth("log", 2)
sum = sum + calculateWorth("blaze rod", 15)
sum = sum + calculateWorth("gunpowder", 3)
sum = sum + calculateWorth("golden apple", 75)
sum = sum + calculateWorth("carrot", 0.6)
sum = sum + calculateWorth("potato", 0.6)
sum = sum + calculateWorth("melon slice", 0.6)
sum = sum + calculateWorth("flint", 0.6)
sum = sum + calculateWorth("totem of undying", 150)
sum = sum + calculateWorth("obsidian", 12)
sum = sum + calculateWorth("quartz", 10)
#modded
sum = sum + calculateWorth("silver", 30)

print("Your inventory is worth: " + str(sum) + "$")