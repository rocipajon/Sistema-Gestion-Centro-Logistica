#FuncionesSG2.py

import random

#Codificación sucursales

# 1 Norte
# 2 Sur
# 3 Oeste
# 4 Caba

def llenadoListas(sucursalSalida,sucursalEnvio,pesoPaquete,envioExpres):
    #Se generan valores automaticos para cada variable
    sucursal=random.randint(1,4)
    llegada=random.randint(1,4)
    peso=random.randint(1,40)
    expres=random.randint(1,4)
    
    #Se guardan los valores
    pesoPaquete.append(peso)
    sucursalSalida.append(sucursal)   
    sucursalEnvio.append(llegada)
    envioExpres.append(expres)

    return (sucursal,llegada,peso,expres)

#Calculo del valor del envío teniendo en cuenta:

#Sucursal de salida, zona de destino, peso y tipo de envío: estandar/express
def calculoEnvio(sucursal,destino,peso,expres):
    costoPorPeso=(peso*1000)
    if sucursal==1:
        if destino==2:
            costoPorPeso=costoPorPeso*1.2
        elif destino==3:
            costoPorPeso=costoPorPeso*1.15
        elif destino==4:
            costoPorPeso=costoPorPeso*1.1
    elif sucursal==2:
        if destino==1:
            costoPorPeso=costoPorPeso*1.2
        elif destino==3:
            costoPorPeso=costoPorPeso*1.15
        elif destino==4:
            costoPorPeso=costoPorPeso*1.1
    elif sucursal==3:
        if destino==1 or destino==2:
            costoPorPeso=costoPorPeso*1.15
        elif destino==4:
            costoPorPeso=costoPorPeso*1.1
    else:
        if destino==1 or destino==2 or destino==3:
            costoPorPeso=costoPorPeso*1.1
    if expres==1:
        costoPorPeso=costoPorPeso*1.3
    costoPorPeso=round(costoPorPeso,2)
    #Calculo el precio del envio dependiendo de las variables 
    return costoPorPeso 

def facturaCliente(sucursal,llegada,peso,expres,costoPaquete):
    #Se genera el detalle de la facturación para el cliente
    salida=0
    destino=0
    rapido=0
    if sucursal==1:
        salida="Zona Norte"
    elif sucursal==2:
        salida="Zona Sur"
    elif sucursal==3:
        salida="Zona Oeste"
    else:
        salida="Zona CABA"
    
    if llegada==1:
        destino="Zona Norte"
    elif llegada==2:
        destino="Zona Sur"
    elif llegada==3:
        destino="Zona Oeste"
    else:
        destino="Zona CABA"
    
    if expres==1:
        rapido="Si"
    else:
        rapido="No"

    #Imprime por pantalla la factura
    print(f"\nSalida: {salida}\nDestino: {destino}\nPeso: {peso}kg\nExpres: {rapido}\nPrecio total: ${costoPaquete}")


#Funciones de validación:

def valida1o2(confirmacion):
    #Validación 1 o 2
    while confirmacion != "1" and confirmacion != "2":
        confirmacion = input("Respuesta inválida. Escriba (1|2): ")

    return confirmacion

def validaSioNo(confirmacion):
    #Validación Si o No
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Respuesta inválida. Escriba (si|no): ").lower()

    return confirmacion

#Recaudación por cada sucursal
def recaudacionSuc(costoPaquete,sucursal,recaudado):
    if sucursal==1:
        aux=recaudado[0]+costoPaquete
        recaudado[0]=aux
    elif sucursal==2:
        aux=recaudado[1]+costoPaquete
        recaudado[1]=aux
    elif sucursal==3:
        aux=recaudado[2]+costoPaquete
        recaudado[2]=aux
    else:
        aux=recaudado[3]+costoPaquete
        recaudado[3]=aux
        
#Generación de envíos
def generarEnvio(sucursalSalida, sucursalEnvio, pesoPaquete, envioExpres, recaudado, facturaMatriz4x4):
    confirmacion = input("\nAgregar un nuevo envio?(si|no): ").lower()
    confirmacion = validaSioNo(confirmacion)

    while confirmacion == "si":
        sucursal, llegada, peso, expres = llenadoListas(sucursalSalida, sucursalEnvio, pesoPaquete, envioExpres)
        costoPaquete = calculoEnvio(sucursal, llegada, peso, expres)

        recaudacionSuc(costoPaquete, sucursal, recaudado)# suma por sucursal
        actualizar_matriz(facturaMatriz4x4, sucursal, llegada, costoPaquete)# suma en la celda [sucursal-1][destino-1]
        facturaCliente(sucursal, llegada, peso, expres, costoPaquete)

        print(f"{sucursalSalida}\n{sucursalEnvio}\n{pesoPaquete}\n{envioExpres}")

        confirmacion = input("\nAgregar un nuevo envio?(si|no): ").lower()
        confirmacion = validaSioNo(confirmacion)
        
#Contador  
def contadorLista(lista):
    maximo=0
    localidad=0
    primero=lista.count(1)                
    segundo=lista.count(2)
    tercero=lista.count(3)
    cuarto=lista.count(4)
    
    for i in range(4):
        if primero>maximo:
            maximo=primero
            localidad="Norte"
        elif segundo>maximo:
            maximo=segundo
            localidad="Sur"
        elif tercero>maximo:
            maximo=tercero
            localidad="Oeste"
        elif cuarto>maximo:
            maximo=cuarto
            localidad="CABA"
    return (maximo,localidad)

#Sucursal de mayor recaudación
def sucMayorReca(recaudado):
    maximo=max(recaudado)
    pos=recaudado.index(maximo)
    if pos==0:
        pos="norte"
    elif pos==1:
        pos="sur"
    elif pos ==2:
        pos="oeste"
    elif pos==3:
        pos="caba"
    return (maximo,pos)

#Matriz
def crear_matriz_4x4():
    return [[0.0 for _ in range(4)] for _ in range(4)]

def actualizar_matriz(m4x4, sucursal, destino, costo):
    m4x4[sucursal - 1][destino - 1] += costo

def imprimir_matriz(m4x4):
    print("-------------------------------------")
    print("SUCURSAL/ZONA DESTINO\t01\t02\t03\t04")
    print("-------------------------------------")
    for i in range(4): 
        print(f"{i+1}\t\t\t{m4x4[i][0]}\t{m4x4[i][1]}\t{m4x4[i][2]}\t{m4x4[i][3]}")
    print("-------------------------------------")
