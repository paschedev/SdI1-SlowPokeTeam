#Escrito por Ovelar Isaias Javier

def juego():
    import random
    puntos=0
    respuesta=0

    #Solo se permiten 3 errores en todo el juego
    intentos=3
    #Diccionario donde se guardan las opciones
    opciones={'a':0,'b':0,'c':0,'d':0}
    jugadas=0
    aciertos=0


    while intentos > 0:
        #Se definen opciones aleatorias
        for key in opciones:
            opciones[key]=random.randint(1,50)
        #Se elige la respuesta aleatoriamente
        respuesta=random.choice(list(opciones.values()))
        while True:
            try:
                print(f"Cual es en decimal el numero {bin(respuesta)} ? ")
                print(f"A- {opciones['a']}  C- {opciones['c']}")
                print(f"B- {opciones['b']}  D- {opciones['d']}")
                print(f"\n\n puntos: {puntos}")
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

                    #El bucle de intento solo se termina al ingresar una opcion valida o invalida, no contempla opciones invalidas
                    break
                else:
                    print("Opcion invalida, solo letras a b c d")

    print(f"Juego terminado!")
    print(f"Jugadas: {jugadas}, aciertos: {aciertos}, Puntos:{puntos}")


juego()

