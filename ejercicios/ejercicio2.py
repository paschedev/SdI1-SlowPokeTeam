# Funciones
#Función que toma el númeor ingresado por el usuario como argumento y lo ingresa como parametro a validar
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    num = int(input(mensaje))
    while num < min or num > max:
        num = int(input(f"Error. {mensaje}"))
    return num

#Toma como argumento el número ya validado y lo pasa al parametro de la funcxión para dividir el número y obtener una lista con los restos
def division_y_resto(numero):
    restos = []  
    while numero > 0:
        resto = numero % 2  
        restos.append(resto)  
        numero = numero // 2  
    return restos

#Esta función se encarga de tomar la lista con los restos como argunmetos e invertirlos, formando una nueva lista
def resto_invertido(restos):
    restos_invertidos = []
    for i in range(len(restos) - 1, -1, -1):  # Desde el último índice hasta el primero
        restos_invertidos.append(restos[i])
    return restos_invertidos

#Esta función toma la lista ya invertida, extrae número por número y lo convierte en una cadena de texto. 
# Luego, imprime el númeor binario como resultado
def decimal_a_binario():
    numero = leer_entero_validado("Ingrese un número natural: ") #Ingresa el númeor del usuario y lo valida
    restos = division_y_resto(numero) #Divide el número y guarda los restos
    restos_invertidos = resto_invertido(restos) #Invierte el orden de los restos
    
    binario = ''.join(map(str, restos_invertidos)) #Covierte la lista en un string
    print(f"El número decimal {numero} es el siguiente binario: {binario}")


#Programa principal
decimal_a_binario()
