##1 Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
num = 21
print (num)

##2 Imprimir el tipo de dato de la constante 8.5
print(type (8.5))

##3 Imprimir el tipo de dato de la variable creada en el punto 1
print(type(num))

##4 Crear una variable que contenga tu nombre
miNombre = 'Wilman Conde'

##5 Crear una variable que contenga un número complejo
numComplejo = 1 + 1j

##6 Mostrar el tipo de dato de la variable creada en el punto 5
print(type(numComplejo))

##7 Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math
piRedondeado = round(math.pi, 4)
print (piRedondeado)

##8 Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
verdad = 'True'
verdadero = True

##9 Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(verdad))
print(type(verdadero))

##10 Asignar a una variable, la suma de un número entero y otro decimal
sumaFlotante = 12 + 3.5

##11 Realizar una operación de suma de números complejos
var1 = 1+3j
var2 = 3+4j
print(var1 + var2)

##12 Realizar una operación de suma de un número real y otro complejo
var1 = 18
var2 = 3+4j
print(var1 + var2)

##13 Realizar una operación de multiplicación
var1 = 18
var2 = 3
print(var1 * var2)

##14 Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2**8
print(potencia)

##15 Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
division = 27 / 4
print(division)

##16 De la división anterior solamente mostrar la parte entera
entero = 27 // 4
print(entero)

##17 De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)

##18 Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
total27 = (entero * 4 ) + resto
print(total27)

##19 Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var1 = 'Hola'
var2 = ' a todos'
print(var1 + var2)

##20 Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
dato = 2=='2'
print(dato)

##21 Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
dato = 2==int('2')
print(dato)

##22 ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Porque la coma no es para numeros decimales. Se usa el punto

##23 Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var3 = 3
var3 -= 5
print(var3)

##24 Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)
# Se mueve el bit alto de la posicion 0 a la posicion 2 con valor de 4 decimal

##25 Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# no se puede realizar la operacion ya que uno es entero y el otro string.
# Si se convierten ambos a string quedaria 22 y si ambos son enteros seria 4

##26 Realizar una operación válida entre valores de tipo entero y string
print('Mi nombre es ' + miNombre + ' y tengo ' + str(total27) + ' años')