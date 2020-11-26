print('Welcome to the TIPZZ CAL')
bill = float(input('What was the total bill? $'))
tip = int(input('What % of tip would you like to give? 10, 15, or 20? '))
persons = int(input('How many people are paying? '))

total_bill = tip / 100 * bill + bill
bill_per_persons = total_bill / persons
final_amt = round(bill_per_persons, 2)
print(f'Each person should pay: ${final_amt}')