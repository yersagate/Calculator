try:
    a = float(input('Number One: '))
    b = float(input('Number Two: '))
except ValueError:
    print("Ошибка: нужно ввести число!")
    exit()

action = input('Action (+ - / *): ')

if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '/':
    if b == 0:
        print("ZERO?!?")
    else:
        print(a / b)
elif action == '*':
    print(a * b)
else:
    print('Wrong action :)')
