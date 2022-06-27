# Empowerment---API
this development proposes the construction of authenticated middleware to consume financial services and persist their preferences


# Empowerment Labs (Business Case)

## Historia de Usuario

- Como comerciante, quiero saber qué símbolos están disponibles para configurar para poder saber cuáles puedo usar.
- Como comerciante, quiero configurar qué símbolos me interesan y cuáles no para poder ver sus precios más tarde en consecuencia.
- Como comerciante, quiero saber los precios disponibles para una acción específica en un período de tiempo determinado para poder analizar más a fondo los datos.
- Como comerciante, quiero descargar todos los datos de todas las acciones en formato csv para poder abrirlos en software de terceros como Microsoft Excel o Google Sheets.

## Requerimientos No Funcionales

- La generación de archivos CSV debe ser un trabajo asíncrono.
- Debe utilizarse DynamoDB como base de datos. Para las otras partes de la arquitectura, se puede usar cualquier lenguaje/marco.}
- Los precios de las acciones se pueden obtener de cualquier API gratuita disponible como Polygon.
- El código entregado debe tener una cobertura de prueba de al menos el 50 % O todos los puntos finales deben estar cubiertos por Postman Flow.
- La API debe protegerse para evitar cargos no deseados o no autorizados.

## Empowerment - API

En un primer MVP este servicio cumple el rol de middware a la vez que administra la interacción con la BD en la cual se persisten las de los usuarios registrados. 

![Untitled Diagram.drawio.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9aec9a9-d8b2-4cd9-8023-f8392f488036/Untitled_Diagram.drawio.png)

Endpoint para extraer las compañias suceptibles a ser trakeadas.

Endpoint para almacenar las preferencias. 

Endpoint para conocer el valor de una acción en un intervalo de tiempo

Endpoint para descargar el reponse como csv

## Polygon

Polygon es un servicio que disponibiliza a sus usuarios los movimientos de acciones registrados en la bolsa de  New York, siendo esta una de las fuentes más usadas para este segmento de negocio en el mundo:  [more information here](https://polygon.io/)

### End Points from Polygon

El listado completo de endpoints de plataforma es listado [aquí](https://polygon.io/system).

Para este busineess case haremos uso de:

- /v2/snapshot/locale/global/markets/forex/tickers : Fuente en MVP de las compañias listadas.
- /v2/reference/news: Notias de la compañia consultada
- /v1/open-close/{stocksTicker}/{date}: Precio de la accción apertura / cierre en eun dia determinado:
    
    Ejemplo de uso:
    
    [Parametros del endpoint](https://www.notion.so/f8ccd35aeeca4f54b3e02499ded4d795)
