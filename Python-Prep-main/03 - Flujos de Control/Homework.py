##1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var1 = int(input('Ingresa un numero '))
if (var1 > 0):
    print('El numero es positivo')
elif (var1 < 0):
    print('El numero es negativo')
else:
    print('El numero es 0')
print()

##2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
var1 = 10
var2 = 2
if (type(var1) == type(var2)):
    print('Las variables son del mismo tipo')
else:
    print('Las variables no son de tipo diferente')
print()

##3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1,21):
    if (i % 2 == 0):
        print(f'{i} es par')
    else:
        print(f'{i} es impar')
print()

##4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(6):
    print(f'El numero {i} elevado a la 3 es {i**3}')
print()

##5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var = 6
for i in range(var):
    print(f'Ciclo {i}')
print()

##6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
var = 10
if (var != int):
    print('EL dato ingresado no es un numero entero')
    if (var > 0):
        num = var
        factorial = 1
        while (num > 0):
            factorial = num * factorial
            num -= 1 
        print(f'Factorial de {var} es {factorial}')
    else:
        print('El numero debe ser entero y mayor a cero')
print()
        
##7) Crear un ciclo for dentro de un ciclo while
ciclo = 5
while (ciclo > 0):
    for i in range(ciclo):
        print(f'Ciclo while {ciclo}')
        print(f'Ciclo for{i}')
    ciclo -= 1
print('Termina')
print()

##8) Crear un ciclo while dentro de un ciclo for
var = 'Anidado'
for i in range(len(var)):
    caracter = var[i]
    print(f'En el indice {i} tenemos las letra {caracter}')
    n = 0
    while (n >= 0):
        n = 0
        n += 1
        print(f'Ciclo while {n}')
        break
print('termina')
print()

##9) Imprimir los números primos existentes entre 0 y 30
var = 30
for i in range(2,var):
    if ((i == 2 or i == 3 or i ==5)) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0):
        print(f'{i} es primo')
print()

##10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

##11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

##12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

##13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
for i in range(100,300):
    while (i % 12 == 0):
        res = i / 12
        print(f'EL numero {i} se puede dividir por 12 => {int(res)}')
        i += 1
        continue
print('termina')
print()

##14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usuario de buscar el siguiente
var = int(input('Ingresa un numero '))
if ((var == 2 or var == 3 or var == 5) or (var % 2 != 0 and var % 3 != 0 and var % 5 != 0)):
    print(f'El numero {var} es primo')
else:
    print(f'El numero {var} no es primo')

##15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
i = 100
while (i < 301):
    if (i % 3 == 0) and (i % 6 == 0):
        print(f'El primer numero entre 100 y 300 divisible por 3 y 6 es =>', i)
        break
    i += 1
