#Ejercicio Nº 4 desarrollado por: Gaston Paschetta
#El programa debe pedir al usuario que ingrese valores binarios (0 o 1)
#Luego debe elegir simular puertas logicas AND, OR y NOT
#Como ampliacion del programa se añaden las puertas NAND, NOR y XOR
#El programa debe mostrar el resultado de la puerta logica elegida

#Funciones
def main():
    print('\nBienvenido al ejercicio 4\n\n')
    puerta = puerta_logica_validada()
    ejecutar_puerta(puerta)

#Funcion que pide al usuario ingresar los valores a evaluar en las puertas logicas y valida que sean 0 o 1
#Es utilizada por las funciones que imprimen las tablas de verdad

def ingresar_valores(puerta):
    print('Ingrese los valores para evaluar en puertas logicas')
    a = int(input('Ingrese el primer valor (0 o 1): '))
    while a not in [0, 1]:
        print('Valor no valido. Ingrese 0 o 1: ')
        a = int(input('Ingrese el primer valor (0 o 1): '))

    if puerta == 3: #En el caso de la puerta NOT, solo se necesita un valor, por lo que se hace un return inmediatamente
        return a, None
    
    b = int(input('Ingrese el segundo valor (0 o 1): '))
    while b not in [0, 1]:
        print('Valor no valido. Ingrese 0 o 1: ')
        b = int(input('Ingrese el segundo valor (0 o 1): '))
    return a, b

#Validacion de la puerta logica elegida por el usuario
#El usuario debe elegir entre las puertas AND, OR, NOT, NAND, NOR y XOR
#(1, 2, 3, 4, 5 y 6 respectivamente)
def puerta_logica_validada():
    print('Elija la puerta logica que desea simular:')
    print('1. AND\t2. OR\t3. NOT\t4. NAND\t5. NOR\t6. XOR')
    puerta = (int(input('Ingrese el numero de la puerta logica: ')))
    while puerta not in [1, 2, 3, 4, 5, 6]:
        print('Opcion no valida. Intente nuevamente:\t1. AND\t2. OR\t3. NOT\t4. NAND\t5. NOR\t6. XOR')
        puerta = int(input('Ingrese el numero de la puerta logica: '))
    return puerta

#Esta funcion ejecuta la puerta logica elegida por el usuario
#Llama a la funciones tabla_[opcion elegida]
def ejecutar_puerta(puerta):
    if puerta == 1: #puerta AND
        tabla_and(puerta)
    elif puerta == 2: #puerta OR
        tabla_or(puerta)
    elif puerta == 3: #puerta NOT
        tabla_not(puerta)
    elif puerta == 4: #puerta NAND
        tabla_nand(puerta)
    elif puerta == 5: #puerta NOR
        tabla_nor(puerta)
    elif puerta == 6: #puerta XOR
        tabla_xor(puerta)

#Las siguientes funciones imprimen cada tabla de verdad
#Piden valores a travez de la funcion ingresar_valores() para posteriormente imprimir la tabla de verdad correspondiente

#AND
def tabla_and(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad AND')
    print('A\tB\tA AND B')
    print(f'{a}\t{b}\t{a and b}')

#OR
def tabla_or(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad OR')
    print('A\tB\tA OR B')
    print(f'{a}\t{b}\t{a or b}')

#NOT
def tabla_not(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad NOT')
    print('A\tNOT A')
    print(f'{a}\t{not a}')

#NAND
def tabla_nand(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad NAND')
    print('A\tB\tA NAND B')
    print(f'{a}\t{b}\t{not (a and b)}')

#NOR
def tabla_nor(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad NOR')
    print('A\tB\tA NOR B')
    print(f'{a}\t{b}\t{not (a or b)}')

#XOR
def tabla_xor(puerta):
    a, b = ingresar_valores(puerta)
    print('Tabla de verdad XOR')
    print('A\tB\tA XOR B')
    print(f'{a}\t{b}\t{a != b}')


#Main
main()