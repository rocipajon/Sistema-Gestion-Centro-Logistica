import random

def llenadoListas():
    sucursalSalida=[]
    sucursalEnvio=[]
    pesoPaquete=[]
 
    paquetes=random.randint(0,20)
    for i in range (paquetes):
        sucursal=random.randint(1,4)
        llegada=random.randint(1,4)
        peso=random.randint(1,40)
        pesoPaquete.append(peso)
        sucursalSalida.append(sucursal)   
        sucursalEnvio.append(llegada)
        
    return(sucursalSalida,sucursalEnvio,pesoPaquete)
            
envio,destino,peso=llenadoListas()

print(envio)
print(destino)
print(peso)

print(f"Cantidad de envios: {len(envio)}")
        
