weight = int(input("Weight: \n"))
korl = input("(K)g or (L)bs: \n").lower()

if korl == "k":
    print("your weight in pounds equals to \n", weight * 2.2)
elif korl == "l":
    print("your weight in Kilograms equals to\n", weight / 2.2)
else:
    print("you may have inserted a bad character \n")
