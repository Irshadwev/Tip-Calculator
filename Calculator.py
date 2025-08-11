print("Welcome to the tip Calculator")
bill= float(input("What was the total bill? $ "))
tip= int(input("How much would you like to give? 10, 12, or 15 "))
persons= int(input('How many people to split the bill?'))
total_tip=tip/100*bill
total_tip_amount=bill+total_tip
amount_per_person=total_tip_amount/persons
total_amount=round(amount_per_person, 2)
print(f'Each person should pay: $ {total_amount}')