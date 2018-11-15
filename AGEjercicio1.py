import random
from deap.tools import cxTwoPoint, mutUniformInt
pob = 50
gananciaT1 = [0.00, 0.28, 0.45, 0.65, 0.78, 0.90, 1.02, 1.13, 1.23, 1.32, 1.38]
gananciaT2 = [0.00, 0.25, 0.41, 0.55, 0.65, 0.75, 0.80, 0.85, 0.88, 0.90, 0.90]
gananciaT3 = [0.00, 0.15, 0.25, 0.40, 0.50, 0.62, 0.73, 0.82, 0.90, 0.96, 1.00]
gananciaT4 = [0.00, 0.20, 0.33, 0.42, 0.48, 0.53, 0.56, 0.58, 0.60, 0.60, 0.60]

sumaApt = 0
T = 0
individuosIni = []
aptitudes = []
valoresEsperados = []


def fAptitud(T1, T2, T3, T4):
    v = abs((T1 + T2 + T3 + T4) - 10)

    aptitud = ((T1 + T2 + T3 + T4) / ((500 * v) + 1))
    return aptitud


def creacionIndividuos():
    for i in range(pob):
        individuosIni.append([random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)])

def calculoAptitudes(individuos):
    aptitudes = []
    valoresEsperados = []
    sumaApt = 0
    T = 0
    for individuo in individuos:
        aptitudes.append(fAptitud(gananciaT1[individuo[0]], gananciaT2[individuo[1]], gananciaT3[individuo[2]], gananciaT4[individuo[3]]))

    for aptitud in aptitudes:
        sumaApt += aptitud

    f = sumaApt/pob

    for aptitud in aptitudes:
        vei = aptitud/f
        valoresEsperados.append(vei)
        T += vei
    
    print("Aptitudes para ésta generación: ")
    print(aptitudes)
    return valoresEsperados

def ruleta(individuos, valoresEsperados):
    nSel = 0
    seleccionados = []
    while pob > nSel:
        r = random.uniform(0, T)
        sumaVE = 0
        print("Valores Esperados: ")
        print(valoresEsperados)
        for n, vei in enumerate(valoresEsperados):
            sumaVE += vei
            if sumaVE >= r:
                nSel += 1
                seleccionados.append(individuos[n])
    return seleccionados

def cruza(seleccionados, tasa_cruza = 0.8):
    aMutar = []
    for i in range(pob):
        r = random.uniform(0,1)
        if r < tasa_cruza:
            aMutar.append(i)

    for n, iPadre in enumerate(aMutar):
        if iPadre == aMutar[-1]:
            seleccionados[iPadre] = cxTwoPoint(seleccionados[iPadre], seleccionados[aMutar[0]])[0]
        else:
            seleccionados[iPadre] = cxTwoPoint(seleccionados[iPadre], seleccionados[aMutar[n + 1]])[0]
    return seleccionados

def mutacion(seleccionados, tasa_mutacion = 0.01):
    for n, individuo in enumerate(seleccionados):
        seleccionados[n] = mutUniformInt(individuo, 0, 10, tasa_mutacion)[0]
    return seleccionados


creacionIndividuos()
print(individuosIni)
valoresEsperados = calculoAptitudes(individuosIni)
nuevosSeleccionados = ruleta(individuosIni, valoresEsperados)
nuevaCruza = cruza(nuevosSeleccionados)
nuevaMutacion = mutacion(nuevaCruza)

for i in range(20):
    print(nuevaMutacion)
    valoresEsperados = calculoAptitudes(nuevaMutacion)
    nuevosSeleccionados = ruleta(nuevaMutacion, valoresEsperados)
    print("Nuevos seleccionados")
    print(nuevosSeleccionados)
    nuevosCruza = cruza(nuevosSeleccionados)
    nuevaMutacion = mutacion(nuevaCruza)

print("Últimos más aptos: ")
print(nuevaMutacion)
valoresEsperados = calculoAptitudes(nuevaMutacion)
print("Valores Esperados últimos: ")
print(valoresEsperados)