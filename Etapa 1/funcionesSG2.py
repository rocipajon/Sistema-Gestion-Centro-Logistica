#FuncionesSG2.py

import random
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
    if costoPorPeso<1500:
        costoPorPeso=1500
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

def recaudacionSuc(costoPaquete,sucursal,recaudado):
    #Calcula el total recaudado por sucursal
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
        
            
def generarEnvio(sucursalSalida, sucursalEnvio, pesoPaquete, envioExpres, recaudado, facturaMatriz4x4):
    confirmacion = input("\nAgregar un nuevo envio?(si|no): ").lower()
    confirmacion = validaSioNo(confirmacion)
    
    while confirmacion == "si":
        sucursal, llegada, peso, expres = llenadoListas(sucursalSalida, sucursalEnvio, pesoPaquete, envioExpres)
        costoPaquete = calculoEnvio(sucursal, llegada, peso, expres)

        recaudacionSuc(costoPaquete, sucursal, recaudado)           # suma por sucursal
        actualizar_matriz(facturaMatriz4x4, sucursal, llegada, costoPaquete)  # suma en la celda [sucursal-1][destino-1]
        facturaCliente(sucursal, llegada, peso, expres, costoPaquete)

        # Debug opcional
        print(f"{sucursalSalida}\n{sucursalEnvio}\n{pesoPaquete}\n{envioExpres}")

        confirmacion = input("\nAgregar un nuevo envio?(si|no): ").lower()
        confirmacion = validaSioNo(confirmacion)
        
        
def contadorLista(lista):
    #buscamos la sucursal que mas envio y la zona que mas recibio
    maximo=0
    localidad=0
    primero=lista.count(1)                
    segundo=lista.count(2)
    tercero=lista.count(3)
    cuarto=lista.count(4)
    
    for i in range(4):
        if primero>maximo:
            maximo=primero
            localidad="norte"
        elif segundo>maximo:
            maximo=segundo
            localidad="sur"
        elif tercero>maximo:
            maximo=tercero
            localidad="oeste"
        elif cuarto>maximo:
            maximo=cuarto
            localidad="caba"
    return (maximo,localidad)

def sucMayorReca(recaudado):
    #busca la cucursal que hizo la mayor recaudacion
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

def crear_matriz_4x4():
    # 4 filas (sucursales 1..4) x 4 columnas (destinos 1..4)
    return [[0.0 for _ in range(4)] for _ in range(4)]

def actualizar_matriz(m4x4, sucursal, destino, costo):
    # sucursal y destino vienen 1..4 -> a índices 0..3
    m4x4[sucursal - 1][destino - 1] += costo

def imprimir_matriz(m4x4):
    print("SUCURSAL/ZONA DESTINO   01      02      03      04")
    for i, fila in enumerate(m4x4, start=1):
        print(str(i) + "                       " +
              str(fila[0]) + "     " +
              str(fila[1]) + "     " +
              str(fila[2]) + "     " +
              str(fila[3]))
    print("--------------------------------------------------")









