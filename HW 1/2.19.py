lemon_cups=float(input("Enter amount of lemon juice (in cups):\n"))
water_cups=float(input('Enter amount of water (in cups):\n'))
agave_cups=float(input("Enter amount of agave nectar (in cups):\n"))
servings=float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', str('{:.2f}'.format(servings)),'servings')
print( str('{:.2f}'.format(lemon_cups)),'cup(s) lemon juice')
print( str('{:.2f}'.format(water_cups)),'cup(s) water')
print( str('{:.2f}'.format(agave_cups)),'cup(s) agave nectar')


servings_new=float(input('\nHow many servings would you like to make?'))

new_lemon=((lemon_cups/servings)*servings_new)
new_water=((water_cups/servings)*servings_new)
new_agave=((agave_cups/servings)*servings_new)


print( str('{:.2f}'.format(new_lemon)),'cup(s) lemon juice')
print( str('{:.2f}'.format(new_water)),'cup(s) water')
print( str('{:.2f}'.format(new_agave)),'cup(s) agave nectar')

print('\nLemonade ingredients - yields', str('{:.2f}'.format(servings_new)),'servings')
print( str('{:.2f}'.format(new_lemon/16)),'gallon(s) lemon juice')
print( str('{:.2f}'.format(new_water/16)),'gallon(s) water')
print( str('{:.2f}'.format(new_agave/16)),'gallon(s) agave nectar')