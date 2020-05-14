import random
 
 
individuos={} #Arreglo de individuos
 
 
 
def distancia(n1,n2):   #Funcion para calcular la distancia entre dos numeros
        d=n1-n2
        return abs(d)
 
 
 
def poblacion_inicial():  #Genera la poblacion inicial. Cada individuo tiene asociado un numero aleatorio entre un rango predeterminado
 
	for individuo in range(n_individuos):
 
		individuos[individuo]=random.uniform(limite_inferior, limite_superior)
 
 
 
 
def seleccion(): #Selecciona el individuo cuyo numero mas se acerco al objetivo. Tambien hace un print con los datos del individuo seleccionado
 
        global numero_seleccionado
 
        distancia_minima=1000000000000000000000000
 
        individuo_seleccionado=0
 
        numero_seleccionado=0
 
        for individuo in individuos:
 
                dis=distancia(individuos[individuo], numero_objetivo)
 
                if dis<distancia_minima:
                        distancia_minima=dis
                        individuo_seleccionado=individuo
                        numero_seleccionado=individuos[individuo]
 
        print("Individuo:", individuo_seleccionado, "Numero del individuo:", individuos[individuo_seleccionado], "Distancia:", distancia_minima)
 
 
def mutacion(): #A cada individuo le asocia un nuevo numero aleatorio, solo que en este caso va a estar oscilando cerca del numero que se selecciono en la seleccion. la magnitud de la oscilacion la determina el usuario
 
        for individuo in individuos:
 
                if not individuo==0:
 
                	individuos[individuo]=random.uniform(numero_seleccionado-rango_mutacion,numero_seleccionado+rango_mutacion)
                else:
                	individuos[individuo]=numero_seleccionado
 
 
#Se ingresan las variables y se da info
print("                              ALGORITMO GENETICO - RodJon")
print("")
print("")
print("Saludos profe, es poco pero es trabajo honesto")
 
n_individuos=int(input("Seleccione la cantidad de individuos por generacion ->"))
n_generaciones=int(input("Seleccione el numero de generaciones limite ->"))
numero_objetivo=float(input("Seleccione el numero objetivo ->"))
rango_mutacion=float(input("Seleccione el rango de mutacion ->"))
print("Seleccione entre que valores oscilaran los valores iniciales de cada individuo. Se admiten numeros negativos.")
limite_inferior=float(input("Limite inferior ->"))
limite_superior=float(input("Limite superior ->"))
 
#BUCLE PRINCIPAL. Genera una poblacion inicial. El bucle se ejecuta una vez para cada generacion. Hace un print del num de la generacion, y ejecuta las funciones
 
poblacion_inicial()
 
for generacion in range(n_generaciones):
        print(generacion)
        seleccion()
        if numero_seleccionado==numero_objetivo: #revisa si se alcanzo el numero objetivo. Si es asi lo avisa y rompe el bucle.
                print("Se alcanzo el numero objetivo")
                break
 
        mutacion()
 
print("Resultado final -->", numero_seleccionado)
 
input()