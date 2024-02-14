# Tip Calculator
# Create a new repository called tip calculator.
# If the bill was EUR150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Make the variables dynamic
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# result should be print ->The total amount that each person will pay is {each_person_bill} euro

# Write your code below this line 👇

total_bill = float(input("What is the total amount spent?"))
total_no_of_people = float(input("How many people eat?"))
mathematical_operator = input("pick amathematical operator[only /and* can be used]:")
precentage_tip = 1.12

match mathematical_operator:
    case "/""*":
        print(input(f"The total amount each person will pay is {round(total_bill/total_no_of_people*precentage_tip, 2)}euros"))

