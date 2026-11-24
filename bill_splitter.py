#Bill Splitter
print("Welcome to the bill splitter app!")
print("This app will help you split the bill among your friends.")
print("********************************************")

running_total = 0

num_of_friends = int(input('enter number of friends: '))

appetizers = float(input("Enter appetizers bill: "))
main_courses = float(input("Enter main courses bill: "))
desserts = float(input("Enter desserts bill: "))
drinks = float(input("Enter drinks bill: "))

running_total += appetizers + main_courses + desserts + drinks
print(f'Total bill so far: {running_total:.2f}')

tip_percentage = float(input("Enter tip percentage: "))
tip = running_total * (tip_percentage / 100)

running_total += tip
print(f'Total with tip: {running_total:.2f}')

final_bill = running_total / num_of_friends
print(f'Bill per person: {final_bill:.2f}')

each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)

print("********************************************")
print("Thank you for using the bill splitter app!")