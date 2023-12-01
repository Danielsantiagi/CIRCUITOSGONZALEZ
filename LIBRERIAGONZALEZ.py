import math
import tkinter as tk

def calcular_atenuacion(potencia_entrada, potencia_salida):
    atenuacion = 10 * math.log10(potencia_salida / potencia_entrada)
    return atenuacion

def calcular_factor_potencia(potencia_activa, potencia_aparente):
    factor_potencia = potencia_activa / potencia_aparente
    return factor_potencia

def frecuencia(R, C):
    return 1 / (2 * math.pi * R * C)

def impedancia_rlc(R, L, C, f):
    omega = 2 * math.pi * f
    Z_R = R
    Z_L = 1j * omega * L
    Z_C = -1j / (omega * C)
    Z = Z_R + Z_L + Z_C
    return Z

def calcular_potencia_activa(voltaje, corriente, factor_potencia):
    potencia_activa = voltaje * corriente * factor_potencia
    return potencia_activa

def calcular_potencia_aparente(voltaje, corriente):
    potencia_aparente = voltaje * corriente
    return potencia_aparente

def calcular_potencia_electrica(voltaje, corriente):
    potencia_electrica = voltaje * corriente
    return potencia_electrica

def calcular_potencia_reactiva(potencia_activa, potencia_aparente):
    potencia_reactiva = (potencia_aparente**2 - potencia_activa**2)**0.5
    return potencia_reactiva

def calcular_tension_electrica(resistencia, corriente):
    tension_electrica = corriente * resistencia
    return tension_electrica

def calcular_frecuencia_compleja(L, C, R):
    frecuencia_compleja = (1 / (2 * math.pi)) * ((1 / (L * C)) - (R / (2 * L)))
    return frecuencia_compleja

def calcular_longitud_onda(frecuencia):
    velocidad_luz = 299792458 # m/s
    longitud_onda = velocidad_luz / frecuencia
    return longitud_onda

def calcular_potencia_energia(tiempo, potencia):
    energia = potencia * tiempo
    return energia

def calcular_trabajo(fuerza, distancia):
    trabajo = fuerza * distancia
    return trabajo

def calcular_velocidad_angular(frecuencia):
    velocidad_angular = 2 * math.pi * frecuencia
    return velocidad_angular

def calcular_periodo(frecuencia):
    periodo = 1 / frecuencia
    return periodo

def display_options():
    print("1. Calcular atenuacion")
    print("2. Calcular factor de potencia")
    print("3. Calcular frecuencia")
    print("4. Calcular impedancia RLC")
    print("5. Calcular potencia activa")
    print("6. Calcular potencia aparente")
    print("7. Calcular potencia electrica")
    print("8. Calcular potencia reactiva")
    print("9. Calcular tension electrica")
    print("10. Calcular frecuencia compleja")
    print("11. Calcular longitud de onda")
    print("12. Calcular potencia energia")
    print("13. Calcular trabajo")
    print("14. Calcular velocidad angular")
    print("15. Calcular periodo")

while True:
    display_options()
    option = int(input("Seleccione una opcion: "))
    if option == 1:
        potencia_entrada = float(input("Ingrese la potencia de entrada: "))
        potencia_salida = float(input("Ingrese la potencia de salida: "))
        atenuacion = calcular_atenuacion(potencia_entrada, potencia_salida)
        print("La atenuacion es:", atenuacion)
    elif option == 2:
        potencia_activa = float(input("Ingrese la potencia activa: "))
        potencia_aparente = float(input("Ingrese la potencia aparente: "))
        factor_potencia = calcular_factor_potencia(potencia_activa, potencia_aparente)
        print("El factor de potencia es:", factor_potencia)
    elif option == 3:
        R = float(input("Ingrese el valor de R: "))
        C = float(input("Ingrese el valor de C: "))
        frec = frecuencia(R, C)
        print("La frecuencia es:", frec)
    elif option == 4:
        R = float(input("Ingrese el valor de R: "))
        L = float(input("Ingrese el valor de L: "))
        C = float(input("Ingrese el valor de C: "))
        f = float(input("Ingrese el valor de f: "))
        Z = impedancia_rlc(R, L, C, f)
        print("La impedancia es:", Z)
    elif option == 5:
        voltaje = float(input("Ingrese el valor del voltaje: "))
        corriente = float(input("Ingrese el valor de la corriente: "))
        factor_potencia = float(input("Ingrese el valor del factor de potencia: "))
        potencia_activa = calcular_potencia_activa(voltaje, corriente, factor_potencia)
        print("La potencia activa es:", potencia_activa)
    elif option == 6:
            voltaje = float(input("Ingrese el valor del voltaje: "))
            corriente = float(input("Ingrese el valor de la corriente: "))
            potencia_aparente = calcular_potencia_aparente(voltaje, corriente)
            print("La potencia aparente es:", potencia_aparente)
    elif option == 7:
        voltaje = float(input("Ingrese el valor del voltaje: "))
        corriente = float(input("Ingrese el valor de la corriente: "))
        potencia_electrica = calcular_potencia_electrica(voltaje, corriente)
        print("La potencia electrica es:", potencia_electrica)
    elif option == 8:
        potencia_activa = float(input("Ingrese el valor de la potencia activa: "))
        potencia_aparente = float(input("Ingrese el valor de la potencia aparente: "))
        potencia_reactiva = calcular_potencia_reactiva(potencia_activa, potencia_aparente)
        print("La potencia reactiva es:", potencia_reactiva)
    elif option == 9:
        resistencia = float(input("Ingrese el valor de la resistencia: "))
        corriente = float(input("Ingrese el valor de la corriente: "))
        tension_electrica = calcular_tension_electrica(resistencia, corriente)
        print("La tension electrica es:", tension_electrica)

    elif option == 10:
        L = float(input("Ingrese el valor de L: "))
        C = float(input("Ingrese el valor de C: "))
        R = float(input("Ingrese el valor de R: "))
        frecuencia_comp = calcular_frecuencia_compleja(L, C, R)
        print("La frecuencia compleja es:", frecuencia_comp)
    elif option == 11:
        frecuencia = float(input("Ingrese el valor de la frecuencia: "))
        longitud_onda = calcular_longitud_onda(frecuencia)
        print("La longitud de onda es:", longitud_onda)
    elif option == 12:
        tiempo = float(input("Ingrese el valor del tiempo: "))
        potencia = float(input("Ingrese el valor de la potencia: "))
        energia = calcular_potencia_energia(tiempo, potencia)
        print("La energia es:", energia)
    elif option == 13:
        fuerza = float(input("Ingrese el valor de la fuerza: "))
        distancia = float(input("Ingrese el valor de la distancia: "))
        trabajo = calcular_trabajo(fuerza, distancia)
        print("El trabajo es:", trabajo)
    elif option == 14:
        frecuencia = float(input("Ingrese el valor de la frecuencia: "))
        velocidad_angular = calcular_velocidad_angular(frecuencia)
        print("La velocidad angular es:", velocidad_angular)
    elif option == 15:
        frecuencia = float(input("Ingrese el valor de la frecuencia: "))
        periodo = calcular_periodo(frecuencia)
        print("El periodo es:", periodo)
    choice = input("¿Desea continuar? (s/n): ")
    if choice.lower() != 's':
        break
         
