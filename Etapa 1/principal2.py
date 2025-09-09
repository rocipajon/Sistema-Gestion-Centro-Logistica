#Principal.py

import funcionesSG2

def recaTotal(recaudado):
    ganancia=sum(recaudado)
    print("-------------------------------------")
    print(f"SUCURSAL\tRECAUDACION\n\nNorte\t\t${recaudado[0]}\nSur\t\t${recaudado[1]}\nOeste\t\t${recaudado[2]}\nCABA\t\t${recaudado[3]}")
    print("-------------------------------------")
    print(f"RECAUDACION TOTAL\t${ganancia}")
    
    
    
def main():

    sucursalSalida=[]
    sucursalEnvio=[]
    pesoPaquete=[]
    envioExpres=[]
    recaudado=[0,0,0,0]

    #Menu principal - Unifiqué inicialización - cierre y menu
    confirmacion="0"
    while confirmacion != "3":
        confirmacion = input("\n1.Envios\n2.Cierre diario\nopcion(1|2): ")

        confirmacion = funcionesSG2.valida1o2(confirmacion)

        if confirmacion == "1":
            #alcance D
            funcionesSG2.generarEnvio(sucursalSalida,sucursalEnvio,pesoPaquete,envioExpres,recaudado)
            
        elif confirmacion == "2":
            sino = input("Quiere realizar el cierre del dia(si|no): ").lower()
            sino = funcionesSG2.validaSioNo(sino)

            if sino == "si":
                cad1="INFORMES"
                cad2=cad1.center(20,"-")
                print(cad2)
                #alcance A
                maximo,localidad=funcionesSG2.contadorLista(sucursalSalida)
                if localidad !=0:
                    print(f"Sucursal que mas envios hizo es la de {localidad} con {maximo} envios")
                #alcance C
                maximo,localidad=funcionesSG2.contadorLista(sucursalEnvio)
                if localidad !=0:
                    print(f"Zona que mas envios recibio es la de {localidad} con {maximo} envios")
                #alcance D
                print(recaudado)
                maximo,pos=funcionesSG2.sucMayorReca(recaudado)
                if maximo!=0:
                    print(f"La sucursal que mas recaudo fue la de zona {pos} con recaudacion de ${maximo}")
                #alcance B
                enviosTotales=(len(sucursalSalida))
                if enviosTotales!=0:
                    print(f"La cantidad total de envios realizados fue de {enviosTotales}")
                #alcance F
                recaTotal(recaudado)
                #alcance E
                
                
                
                
                
                
                confirmacion = "3"
       
    
                


    



if __name__  == '__main__':
    main()
