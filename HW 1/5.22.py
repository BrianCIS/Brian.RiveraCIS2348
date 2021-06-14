print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")
first=input('Select first service:\n')
second=input('Select second service:\n')
total=0
cost = {"-": 0, "oil change.lower": 35, "tire rotation.lower": 19, "car wash.lower": 7, "car wax.lower": 12}
print("\nDavy's auto shop invoice\n")
if(first.lower()=='oil change') :
    print("Service 1: Oil change, $35")
    total=total +35

elif(first.lower()=='car wax'):
    print('Service 1: Car wax, $12')
    total = total+12
elif(first.lower()=='tire rotation'):
    print('Service 1: Tire rotation, $19')
    total = total+19
elif(first.lower()=='car wash'):
    print('Service 1: car wash, $7')
    total = total+7
elif(first.lower()=='-'):print('Service 1: No service')

if(second.lower()=='oil change') :
    print("Service 2: Oil change, $35")
    total = total+35
elif(second.lower()=='car wax'):
    print('Service 2: Car wax, $12')
    total = total+12
elif(second.lower()=='tire rotation'):
    print('Service 2: Tire rotation, $19')
    total = total+19
elif(second.lower()=='car wash'):
    print('Service 2: Car wash, $7')
    total = total+7
elif(second.lower()=='-'):print('Service 2: No service')


print ('\nTotal: $'+str(total))