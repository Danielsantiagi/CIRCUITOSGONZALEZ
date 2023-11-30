import math

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
