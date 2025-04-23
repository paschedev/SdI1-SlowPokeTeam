# Ejercicio 1 elaborado por: Karina Rodriguez
# Tabla de verdad

def reconocer_variables(formula):
    # Reconocer que variables posee la formula
    variables = []
    if 'A' in formula:
        variables.append('A')
    if 'B' in formula:
        variables.append('B')
    if 'C' in formula:
        variables.append('C')
    return variables    

def calcular_combinaciones(variables):
    # Calcular la cantidad de combinaciones posibles que tendra la tabla
    combinaciones = 2**len(variables)
    return combinaciones

def generar_tabla_completa(combinaciones, variables):
    table = []
    for i in range(combinaciones):
        # transforma la posicion en binario (cortando el "0b" de la representacion del binario) con bin()
        # y rellena con ceros de acuerdo a la cantidad de variables q haya usando zfill()          
        # Ejemplo: i = 1 -> '001' (si hay 3 variables) 
        binario = bin(i)[2:].zfill(len(variables))
        # Se crea un segundo array con los valores del binario
        tableRows = []
        for j in range(len(binario)): 
            tableRows.append(int(binario[j]))   
        # Se agrega el array para ir armando la tabla (matriz)
        table.append(tableRows)   

    return table   

def generar_tabla_parcial(variables):
    print('Ingrese los valores de las variables:')
    row = []
    for i in range(len(variables)):
        # Se solicita al usuario el valor de cada variable
        value = int(input(f'{variables[i]} = '))
        # Se agrega el valor de la variable al array 
        row.append(value)
    # Se devuelve la matriz de una sola fila
    return [row] 

def imprimir_tabla(tabla, variables, formula):
    variable_values = {}
    # Imprimir los nombres de las variables
    print(f'{' | '.join(variables)} | f= {formula}')
    print('------'*len(variables))
    for i in range(len(tabla)):
        # Asignar a cada variable su valor correspondiente para evaluarlo
        for j in range(len(variables)):
            variable_values[variables[j]] = tabla[i][j]

        # Imprimir los valores de las variables y el resultado de la formula
        if len(variables) == 1:
            print(f'{tabla[i][0]} | {int(eval(formula,variable_values))}')
        elif len(variables) == 2:
            print(f'{tabla[i][0]} | {tabla[i][1]} | {int(eval(formula,variable_values))}')
        elif len(variables) == 3:
            print(f'{tabla[i][0]} | {tabla[i][1]} | {tabla[i][2]} | {int(eval(formula,variable_values))}')

def formula_es_valida(formula):
    # Variables y operadores permitidos
    variables_permitidas = ['A', 'B', 'C']
    operadores_permitidos = ['and', 'or', 'not']
    # Separar la formula en partes
    # Agrega espacios antes y despues de los parentesis para separlos de variable
    # ya que de otra forma toma un (A, por ejemplo, como invalido
    partes = formula.replace('(', '( ').replace(')', ' )').split()
    # Bandera para saber si la formula es valida
    is_clean = True

    # Verificar si la formula contiene solo variables, operadores y parentesis
    for i in range(len(partes)):
        if partes[i] not in variables_permitidas and partes[i] not in operadores_permitidos and partes[i] != '(' and partes[i] != ')':
            print(f'El simbolo "{partes[i]}" no es valido.')
            is_clean = False
            break

    # Verificar si la formula tiene la estructura correcta, no debe empezar ni terminar con un operador
    if partes[0] in ['and', 'or'] or partes[-1] in ['and', 'or']:
        is_clean = False

    return is_clean

def main():
    print('Ingrese la formula:')
    formula = input('f = ')

    if not formula_es_valida(formula):
        print('La formula ingresada no es valida.')
        print('-------------------------------------------------------------------------\n')
        return

    print('\nDesea ingresar valores para las variables? (si/no)')
    print('Si ingresa "no", se mostrara la tabla de verdad completa.')
    respuesta = input('Respuesta: ')
    print('-------------------------------------------------------------------------\n')

    while respuesta.lower() != 'si' and respuesta.lower() != 'no':
        print('La respuesta debe ser "si" o "no"')
        respuesta = input('Respuesta: ')

    if respuesta == 'si':
        # Reconocer variables
        variables = reconocer_variables(formula)
        if len(variables) == 0:
            print('No se ingresaron variables en mayuscula.')
            return
        # Generar tabla parcial y pedir valores
        tabla = generar_tabla_parcial(variables)
        # Imprimir tabla
        print('Tabla de verdad parcial:')
        imprimir_tabla(tabla, variables, formula)                   

    elif respuesta == 'no':
        # Reconocer variables
        variables = reconocer_variables(formula)  
        if len(variables) == 0:
            print('No se ingresaron variables en mayuscula.')
            return      
        # Calcular cantidad de combinaciones
        combinaciones = calcular_combinaciones(variables)
        # Generar tabla completa
        tabla = generar_tabla_completa(combinaciones, variables)        
        # Imprimir tabla
        print('Tabla de verdad completa:')
        imprimir_tabla(tabla, variables, formula)

    print('-------------------------------------------------------------------------\n')

def run():
    # Detalles y explicacion del programa
    print('#########################################################################')
    print('Bienvenido a la tabla de verdad!')
    print('-------------------------------------------------------------------------')
    print('Instrucciones:')
    print('- Se puede ingresar hasta 3 variables (A, B o C), en mayuscula.')
    print('- Operadores permitidos: and, or, not. Respetar minusculas.')
    print('- Se puede ingresar parentesis para indicar prioridad.')
    print('Ejemplo: A and B or not C.')
    print('-------------------------------------------------------------------------\n')
    # Ejecutar funcion principal
    repeat = True

    while repeat:
        main()
        # Opción para volver a utilizar el programa
        print('Desea ingresar otra formula? (si/no)') 
        respuesta = input('Respuesta: ')

        if respuesta.lower() == 'no':
            break
        elif respuesta.lower() == 'si':
            print('-------------------------------------------------------------------------\n')
        else:
            print('No entendi su respuesta. Abortando mision por seguridad!!')
            break

    print('Gracias por usar la tabla de verdad! =D')
    print('#########################################################################')

