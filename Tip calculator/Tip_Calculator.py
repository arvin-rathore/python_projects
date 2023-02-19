# Tip Calculator helps you find the perfect tip for the table bussers 
# according to your preffered percentage fo tip 

print ("Welcome to tip calculator")
# Greets the USER.
bill = float(input("What was the total bill? $\n"))
# Asks the USER how much the bill was and takes (it as input).
tip = int(input("How much would you like to tip?\n"))
# Asks the USER how much percentage of the total bill he/she would like to tip (takes it as input).
people = int(input("How many people are there to split the bill?\n"))
# Asks how many people the USER shared his/her meal with .
# (so that the bill (including the tip) gets divided equally).
tip_as_percentage = tip/100
# Takes the USER preffered tip percentage. 
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
# Adds the tip precentage to the total bill.
bill_per_person = total_bill/people
# Calculates how much each person should pay for the total bill.
# Here (total bill = bill + tip).
final_amount = round(bill_per_person, 2)
final_amount = format(bill_per_person)
print(f"Each person should pay about: ${final_amount}")
# Tells the USER how much each person should pay including the tip
quit()
# End of the program