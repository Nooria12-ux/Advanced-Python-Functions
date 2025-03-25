lower = int(input("Enter the Lower Limit: "))
upper= int(input("Enyter the Upper Limit: "))

num = [i for i in range(lower, upper + 1)]

print(f"Number lsit: {num}")

even = [i for i in num if i % 2 == 0]
odd = [i for i in num if i % 2 != 0]

print(f"Even Values: {even}")
print(f"Odd Values: {odd}")

#=====================================================

fruits = ["grapefruit", "watermelon", "lichi", "mango", "papaya"]

capFruit = [fruit.capitalize() for fruit in fruits]
upperFruit = [fruit.upper() for fruit in fruits]

print(capFruit)
print(upperFruit)