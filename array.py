# Arrays in arrays
shopping = [
    ["rice", "vegetables", "spaghetti", "meat", "yam"],
    ["beer", "wine", "juice", "yoghurt"],
    ["shoes", "t shirts", "glasses"],
    ["programming books", "internet service"],
]

# print vegetables, glasses, internet service, shoes, juice, meat
print(shopping[0][1])
print(shopping[2][2])
print(shopping[3][1])
print(shopping[2][0])
print(shopping[1][2])
print(shopping[0][3])

print(shopping.count("juice"))
