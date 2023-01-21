# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades = ['col', ' mex', 'ale', 'ing', 'bra']
print(f'lista ciudades =>', ciudades)
print()

# 2) Imprimir por pantalla el segundo elemento de la lista
print(f'segundo elemento de la lista =>', ciudades[1])
print()

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(f'ciudades del 2do al 4to elemento =>', ciudades[1:4])
print()

# 4) Visualizar el tipo de dato de la lista
print(f'tipo de dato del elemento en la posicion 2 =>', type(ciudades[2]))
print()

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(f'elementos a partir del 3ro en adelante =>', ciudades[2:])
print()

# 6) Visualizar los primeros 4 elementos de la lista
print(f'primeros 4 elementos =>', ciudades[:4])
print()

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append('sui')
ciudades.append('col')
print(f'con .append se agregan "sui" y "col" a ciudades =>', ciudades)
print()

# 8) Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(3,'fra')
print(f'con .insert se agrega "fra" en la posicion 4 de ciudades =>\n', ciudades)
print()

# 9) Concatenar otra lista a la ya creada
nombres = ['juan', 'pedro', 'simon', 'javier']
print(f'nueva lista nombres =>', nombres)
ciudades.extend(nombres)
print(f'con .extend se concatena nombres a ciudades =>\n', ciudades)
print()

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad? ==>> muestra el indice del primer elemento encontrado en la lista
print(f'con .index se localiza la posicion del elemento "col" en ciudades =>', ciudades.index('col'))
print()

# 11) ¿Qué pasa si se busca un elemento que no existe?  
# ciudades.index('per')  ==>> muestra un valueError
print(f'se intenta buscar "per" en ciudades y muestra ValueError al no estar en ciudades =>\n', ciudades)
print()

# 12) Eliminar un elemento de la lista
ciudades.remove('fra')
print(f'con .remove se elimina "fra" de ciudades =>\n', ciudades)
print()

# 13) ¿Qué pasa si el elemento a eliminar no existe?
# ciudades.remove('fra')  ==>> muestra un valueError
print(f'se intenta eliminar "fra" de ciudades y da ValueError al no estar en la lista')
print('se debe crear una estructura if para evitar el valueError \nif ("fra" in ciudades):\n    ciudades.remove("fra")')
print()

# 14) Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo
print(ciudades)
var = ciudades.pop()
print(f'con .pop se extrae el ultimo elemento de ciudades y se guarda en otra variable =>', var)
print()

# 15) Mostrar la lista multiplicada por 4
print(f'lista ciudades X 4 =>', ciudades * 4)
print()

# 16) Crear una tupla que contenga los números enteros del 1 al 20
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(f'tupla numeros =>', numeros)
print()

# 17) Imprimir desde el índice 10 al 15 de la tupla
print(f'tupla desde el indice 10 al 15 =>', numeros[10:16])
print()

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(f'con .index(20) se evalua si esta el numero 20 en la tupla. Posicion =>', numeros.index(20))
# print(numeros.index(30))  ==>> muestra un valueError
print(f'con .index(30) se evalua si esta el 30 pero muestra un ValueError al no estar en la tupla')
print()

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print(f'con .index se evalua si esta "Paris" en la lista ciudades y se muestra un ValueError al no estar =>\n', ciudades)
# ciudades.index('Paris')  ==>> muestra un valueError
ciudades.append('Paris')
print(f'con .append se agrega "Paris a la lista =>\n', ciudades)
print()

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(f'con .count se muestra cuantas veces esta "col" en la lista ciudades => ', ciudades.count('col'))
print(f'con .count se muestra cuantas veces esta el 12 en la tupla numeros => ', numeros.count(12))
print()

# 21) Convertir la tupla en una lista
numeros = list(numeros)
print(f'numeros = list(numeros) se convierte la tupla numeros en lista. \nTipo =>', type(numeros), numeros)
numeros = tuple(numeros)
print()

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
var1, var2, var3, *_ = numeros
print(f'se desempaquetan los primeros 3 numeros de la tupla =>\nVar1 =>', var1,'\nVar2 =>', var2, '\nVar3 =>', var3)
print(_)
print()

# 23) Crear un diccionario utilizando la lista creada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario = {'ciudad':[ciudades], 'nombres':[nombres], 'numeros':[numeros]}
print('diccionario = {"ciudad":[ciudades], "nombres":[nombres], "numeros":[numeros]} =>\nSe crea diccionario a partir de las 3 listas creadas anteriormente =>\n', diccionario)

# 24) Imprimir las claves del diccionario
print(f'diccionario.keys() => imprime las claves del diccionario =>\n', diccionario.keys())

# 25) Imprimir las ciudades a través de su clave
print(f'diccionario.values() => imprime los valores del diccionario =>\n', diccionario.values())