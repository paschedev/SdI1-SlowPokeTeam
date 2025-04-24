# Se importa el modulo time para usar retardos
import time 

print("Contador Binario con LEDs:\n")

#Bucle para recorrer del 0 al 15
for i in range(16):
    binario = bin(i)[2:].zfill(4)   
    leds = ''.join(['●' if bit == '1' else '○' for bit in binario]) # Representacion visual con LEDs segun los bits
    print(f"{i:2} -> {binario}  [{leds}]") 

    time.sleep(1) #Pausa de 1 segundo entre cada numero
