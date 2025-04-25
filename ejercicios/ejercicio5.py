#Contador binario hecho por Celeste Monsalbe
#Se importa el modulo time para usar retardos
import time

#Funcion que genera los leds
def mostrar_led(numero, bits=4, retardo= 0.2):
    binario = bin(numero)[2:].zfill(bits)
    led_line = f"{numero:>2} -> {binario}  ["
    for bit in binario:
        led = "●" if bit == '1' else "○"
        led_line += led
        time.sleep(retardo)
    led_line += "]"
    return led_line

#Funcion principal que realiza el conteo binario
def contador_binario():
    bits = 4
    total = 16
    ancho_contenido = 20 + bits  

    #Imprime la parte superior del marco
    print("+------------------------------+")
    print("|  Contador Binario con LEDs   |")
    print("+------------------------------+")

    #Muestra los numeros dentro del marco
    for i in range(total):
        linea = mostrar_led(i, bits)
        print("|    " + linea.ljust(ancho_contenido - 1) + "   |")

    #Imprime la parte inferior del marco
    print("+" + "------------------------------" + "+")
    