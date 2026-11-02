# create calculator
print('let\'s start!')
num1 = int(input('Enter your first number:'))
num2 = int(input('Enter your first number:'))

# math operation
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# final result
print(f'{num1} + {num2} = {addition}')
print(f'{num1} - {num2} = {subtraction}')
print(f'{num1} * {num2} = {multiplication}')
print(f'{num1} / {num2} = {division:.2f}')
print('End of the program, Good luck:)')
