# Sistema de Gestion para Centro de Logistica
Sistema para la gestión de operaciones de recepción y envío de paquetería en un centro de logística. 

OBJETIVO DEL PROYECTO:

El objetivo del proyecto es desarrollar un sistema para la gestión de operaciones de recepción y envío de paquetería en un centro de logística, que permitirá registrar paquetes, asignarlos a rutas de distribución, y almacenar la información para su posterior consulta. También se encargará de calcular el costo de envío teniendo en cuenta, precio por kg, distancia de envío y tipo de envío.
Con ello se buscará mejorar el control de los envíos para reducir errores, optimizar la gestión operativa, aumentar la eficiencia en el cálculo de los costos de envío y mejorar la experiencia de los usuarios.

ALCANCE:

Un sistema de gestión de un centro de logística desea realizar la recaudación diaria de sus ventas y generar automáticamente una factura para el cliente.
-La distribución de paquetería se realiza en sucursales de salida codificadas del 1 al 4, las cuales reparten los paquetes hacia las siguientes zonas de destino, codificadas también del 1 al 4: Zona Norte (1), Zona Sur (2), Zona Oeste (3) y CABA (4).
-El usuario realizará la carga de envíos. El ingreso de los datos se realizará de forma aleatoria y automática. Se dispone de la cantidad de paquetes distribuídos y el peso de cada uno. La carga finalizará cuando el usuario ingrese “No”.
-El envío express y el estándar se encuentran codificados del 1 al 4, siendo el envío express 1 (Con un 25% de probabilidad) y el estándar del 2 al 4.
No se encuentran limitaciones en cuanto a distribución entre zonas.

El centro de distribución establece sus costos de envíos en base a los siguientes criterios:
-Precio por kg: $1000.
-Monto mínimo cobrable por envío: $1500.
-Precio base: precio por kg * peso + recargos.

-Recargos:
  -Envío exprés: +30% del precio por kg.
  -Distancia de envio:
    Zona Sur-Zona Norte (ida y vuelta): +20%
    Zona Sur-Zona Oeste (ida y vuelta): +15%
    Zona Oeste-Zona Norte (ida y vuelta): +15%
    Zona Sur/Norte/Oeste-CABA (ida y vuelta): +10%

Se desea informar:

a)Sucursal que más envíos realizó.
b)Sucursal que más dinero recaudó.
c)Zona que más envíos recibió.
d)Total recaudado por sucursal:

SUCURSAL/ZONA DESTINO    01          02         03         04
     1              XXXX.XX     XXXX.XX    XXXX.XX    XXXX.XX
     2              XXXX.XX     XXXX.XX    XXXX.XX    XXXX.XX
     3              XXXX.XX     XXXX.XX    XXXX.XX    XXXX.XX
     4              XXXX.XX     XXXX.XX    XXXX.XX    XXXX.XX

e)Total recaudado entre todas las sucursales:

SUCURSAL      RECAUDACIÓN
1                 XXXX.XX
2                 XXXX.XX
3                 XXXX.XX
4                 XXXX.XX
-----------------------------
RECAUDACIÓN TOTAL  XXXX.XX

f)Cantidad total de envíos realizados.
