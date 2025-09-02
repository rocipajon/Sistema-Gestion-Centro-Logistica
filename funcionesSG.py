import random
# 1 Norte
# 2 Sur
# 3 Oeste
# 4 Caba
def llenadoListas(sucursalSalida,sucursalEnvio,pesoPaquete,envioExpres):
    sucursal=random.randint(1,4)
    llegada=random.randint(1,4)
    peso=random.randint(1,40)
    expres=random.randint(1,4)
    pesoPaquete.append(peso)
    sucursalSalida.append(sucursal)   
    sucursalEnvio.append(llegada)
    envioExpres.append(expres)
    return(sucursal,llegada,peso,expres)

def calculoPersona(s,d,p,e):
    costoPorPeso=(p*1000)
    if s==1:
        if d==2:
            costoPorPeso=costoPorPeso*1.2
        elif d==3:
            costoPorPeso=costoPorPeso*1.15
        elif d==4:
            costoPorPeso=costoPorPeso*1.1
    elif s==2:
        if d==1:
            costoPorPeso=costoPorPeso*1.2
        elif d==3:
            costoPorPeso=costoPorPeso*1.15
        elif d==4:
            costoPorPeso=costoPorPeso*1.1
    elif s==3:
        if d==1 or d==2:
            costoPorPeso=costoPorPeso*1.15
        elif d==4:
            costoPorPeso=costoPorPeso*1.1
    else:
        if d==1 or d==2 or d==3:
            costoPorPeso=costoPorPeso*1.1
    if e==1:
        costoPorPeso=costoPorPeso*1.3    
    return(costoPorPeso)

def facturaCliente(sucursal,llegada,peso,expres,costoPaquete):
    salida=0
    destino=0
    expres=0
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
        espres="Si"
    else:
        expres="No"
    
    print(f"\nSalida: {salida}\nDestino: {destino}\nPeso: {peso}kg\nExpres: {expres}\nPrecio total: {round(costoPaquete,2)}")
    
    
    
def inicializacion():   
    sucursalSalida=[]
    sucursalEnvio=[]
    pesoPaquete=[]
    envioExpres=[]
    confirmacion=input("\nAgregar un nuevo envio?(si|no): ").lower()
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Respuesta inválida. Escriba (si|no): ").lower()
    while confirmacion=="si":
        sucursal,llegada,peso,expres=llenadoListas(sucursalSalida,sucursalEnvio,pesoPaquete,envioExpres)
        costoPaquete=calculoPersona(sucursal,llegada,peso,expres)
        facturaCliente(sucursal,llegada,peso,expres,costoPaquete)
        print(f"{sucursalSalida}\n{sucursalEnvio}\n{pesoPaquete}\n{envioExpres}")
        confirmacion=input("\nQuiere agregar otro envio?(si|no): ").lower()
    menu()
    
def cierre():
    confirmacion=input("Quiere realizar el cierre del dia(si|no):")
    while confirmacion != "si" and confirmacion != "no":
        confirmacion = input("Respuesta inválida. Escriba (si|no): ").lower()
    if confirmacion=="no":
        menu()
    else:
        print("cierre")
        
def menu():
    confirmacion=input("\n1.Envios\n2.Cierre diario\nopcion(1|2): ")
    while confirmacion != "1" and confirmacion != "2":
        confirmacion = input("Respuesta inválida. Escriba (1|2): ")
    if confirmacion =="1":
        inicializacion()
    else:
        cierre()

        


    
menu()





        
