import math

height=int(input('Enter wall height (feet):\n'))
width=int(input('Enter wall width (feet):\n'))
area=(width*height)
print('Wall area:', area, 'square feet')
paint_gallon= 350
gallon= (area/paint_gallon)

print('Paint needed:','{:.2f}'.format(gallon), 'gallons')

cans=math.ceil(gallon)
print('Cans needed:', cans,'can(s)')
