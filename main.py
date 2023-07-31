# Datos primitivos simples

numero_entero = 18
numero_real = 17.1
cadena = "Hola Mundo"
boleano = True

cadena_total = cadena + ", " + str(numero_entero) + ", " + str(numero_real) + ", " + str(boleano)

# Maximos enteros y flotantes en python

"""Para el caso de los enteros, no existe limite determinado por Python 3, el valor máximo que puede
 alcanzar un entero dependerá de la capacidad de la máquina para almacenarlo"""

"""En el caso de los flotantes sí que hay un limite establecido por temas de lo preciso que puede ser
representar números en 'coma flotante', la mínima precisión es 2.2250738585072014e-308, y la máxima
precisión es 1.7976931348623157e+308. En el caso de colocar un valor fuera de este rango se definirá automáticamente
como infinito (inf)"""

# Suma de los primeros n numeros pares
suma_pares = numero_entero//2*(numero_entero//2+1)

print(cadena_total)
print(suma_pares)



