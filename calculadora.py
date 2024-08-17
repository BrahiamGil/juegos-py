#Calculadora 

print('Calculadora')

while True:
    numero1 = float(input('Ingresa el primer numero'))

    operacion = input('Ingresa la operacion: + , - , * , / ')

    numero2 = float(input('Ingresa el segundo numero'))

    if operacion == '+':
        print('El resultado es: ', numero1 + numero2)
    elif operacion == '-':
        print('El resultado es: ', numero1 - numero2)
    elif operacion == '*':
        print('El resultado es: ', numero1 * numero2)
    elif operacion == '/':
        print('El resultado es:', numero1 / numero2)