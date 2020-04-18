# Develop a logic that reads the weight and the height of a person, calculate their BMI and show their status,
# according to the table below. under 18.5: underweight; between 18.5 and 25: ideal weight; 25 to 30: overweight; 30 to
# 40: obesity; Above 40: morbid obesity.

w = float(input('Enter the Weight in Kg: '))
h = float(input('Enter the Height in m: '))
BMI = w / pow(h, 2)
print('The BMI is: {:.1f}'.format(BMI))
if BMI < 18.5:
    print('It is UNDER weight')
elif 18.5 <= BMI < 25:
    print('It is IDEAL weight')
elif 25 <= BMI < 30:
    print('It is OVER weight')
elif 30 <= BMI < 40:
    print('It is OBESITY')
else:
    print('It is MORBID OBESITY')
