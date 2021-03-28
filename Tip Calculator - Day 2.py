# This is a Day 2 Project!
print("Welcome to the tip calculator.")

#Total bill
total_bill = input("What is the total bill?: $")
int_total_bill = float(total_bill)

#Tip Percentage
tip_percentage = input("What percentage tip would you like to give? ")
int_tip_percentage = int(tip_percentage)

#Total  tip
total_tip = int_total_bill * (int_tip_percentage / 100)

#Total After Tip
total_after_tip = int_total_bill + total_tip

#Bill Split
bill_split = input("How many people to split the bill? ")
int_bill_split = int(bill_split)

#Each Person Payment
each_payment = total_after_tip / int_bill_split
round_each_payment = "{:.2f}".format(each_payment)
# round_each_payment = round(each_payment, 2)

#Result
end_result = f"Each person should pay : ${round_each_payment}"
print(end_result)