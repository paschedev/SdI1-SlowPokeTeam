#Escrito por Ovelar Isaias Javier
from time import sleep
def juego_run():
    import random
    import os
    puntos=0
    respuesta=0

    #Solo se permiten 3 errores en todo el juego
    intentos=3
    #Diccionario donde se guardan las opciones
    opciones={'a':0,'b':0,'c':0,'d':0}
    jugadas=0
    aciertos=0

    print("El juego consiste en adivinar dentro de 4 opciones en decimal, cual corresponde a un numero en binario")
    print("Solo se permiten 3 intentos fallidos en general, cada acierto otorga 1000 puntos")
    continuar=input("Presione una tecla para continuar")
    while intentos > 0:
        #Se definen opciones aleatorias
        for key in opciones:
            opciones[key]=random.randint(1,50)
        #Se elige la respuesta aleatoriamente
        respuesta=random.choice(list(opciones.values()))
        while True:
            try:
                os.system("cls")
                print(f"Cual es en decimal el numero {bin(respuesta)} ? ")
                print(f"A- {opciones['a']}  C- {opciones['c']}")
                print(f"B- {opciones['b']}  D- {opciones['d']}")
                print(f"\n\n puntos: {puntos} | Intentos disponibles: {3-intentos}")
                eleccion=input()
            except ValueError:
                print("Solo se aceptan letras a b c d")
            else:
                if eleccion in 'abcd':
                    if respuesta==opciones[eleccion]:
                        print("Respuesta correcta!")
                        puntos+=1000
                        aciertos+=1
                    else:
                        print("Respuesa incorrecta")
                        intentos-=1
                    jugadas+=1
                    if intentos > 0:
                        sleep(2.5)
                    #El bucle de intento solo se termina al ingresar una opcion valida o invalida, no contempla opciones invalidas
                    break
                else:
                    print("Opcion invalida, solo letras a b c d")

    print(f"Juego terminado!")
    print(f"Jugadas: {jugadas}, aciertos: {aciertos}, Puntos:{puntos}")