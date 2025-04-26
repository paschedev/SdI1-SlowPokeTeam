# IMPORTACION DE CARPETA DE EJERCICIOS
import sys
sys.path.append('./ejercicios')

# IMPORTACIONES DE MODULOS
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5

"""
    Presentacion del Trabajo Practico
    Contiene el menu principal a los ejercicios realizados por los integrates del grupo.
"""
def menu():
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('- - - - - - - -  TP Grupal de Integracion  - - - - - - - -')
    print('- - - - - - - - - -   Grupo SlowPoke   - - - - - - - - - -')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

    # MENU
    # Se presentan los ejercicios disponibles, el usuario ingresa una opcion y se ejecuta el ejercicio correspondiente
    # El menu se repite hasta que el usuario ingrese la opcion 0
    opcion = ''

    while opcion != '0':
        print('Ejercicios disponibles (ingrese el numero del ejercicio):')
        print('')
        print('1. Ejercicio 1 - Tabla de verdad')
        print('2. Ejercicio 2 - Conversor decimal a binario')
        print('3. Ejercicio 3 - Juego: Adivina el numero!')
        print('4. Ejercicio 4 - Compuertas logicas')
        print('5. Ejercicio 5 - Contador binario')
        print('0. Salir')

        opcion = input('Ingrese una opcion: ')

        match opcion:
            case '1':
                ejercicio1.run()
            case '2':
                ejercicio2.decimal_a_binario()
            case '3':
                ejercicio3.juego_run()
            case '4':
                ejercicio4.main()
            case '5':
                ejercicio5.contador_binario()
            case '0':
                print('Gracias por usar nuestro programa! Vuelve pronto!')
                break
            case _:
                print('No es una opcion valida. Intente nuevamente.')
                
        print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')


# EJECUCION DEL MENU PRINCIPAL
menu()