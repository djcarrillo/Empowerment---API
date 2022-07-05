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

## End Points

Para satisfacer los requerimientos de usuario se un servicio propone dockerizado sobre GCP (docker run) que disponibilice 5 end points tipo get y dos tipo post. 

### Verbos tipo GET:

- Server status: {{baseUrl}}/empowerment/test
- Symbols disponibles: {{baseUrl}}/empowerment/available_symbols
- Precio de Symbols: {{baseUrl}}/empowerment/price_symbol?symbols=nisi amet&date=tempor laboris nulla&adjusted=ullamco dolore
- Consulta de compañia favorita: {{baseUrl}}/empowerment/price_symbol?symbols=nisi amet&date=tempor laboris nulla&adjusted=ullamco dolore
- Consulta de todas las compañias de interes: {{baseUrl}}/empowerment/extract_all?date=tempor laboris nulla:

### Verbos tipo POST:

- creación de un nuevo usuario: {{baseUrl}}/empowerment/created_user?id=ipsum esse sit
- update de compañias favoritas: {{baseUrl}}/empowerment/send_favorite_companies?id=ipsum esse sit

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/40d15d42-d102-49d8-972b-95b6e1209223/Untitled.png)

                                                            colección en postman

Es importante mencionar que todas los endpoints son autenticados, y para este mvp, el token de autenticación se ha fijado a ”xx”

## Fuentes

### Polygon

Polygon es un servicio que disponibiliza a sus usuarios los movimientos de acciones registrados en la bolsa de  New York, siendo esta una de las fuentes más usadas para este segmento de negocio en el mundo:  [more information here](https://polygon.io/)

### End Points from Polygon

El listado completo de endpoints de plataforma es listado [aquí](https://polygon.io/system).

Para este busineess case haremos uso de:

- /v2/snapshot/locale/global/markets/forex/tickers : Fuente en MVP de las compañías listadas.
- /v2/reference/news: Notias de la compañia consultada
- /v1/open-close/{stocksTicker}/{date}: Precio de la acción apertura / cierre en eun dia determinado:
    
    Ejemplo de uso:
    
    [Parametros del endpoint](https://www.notion.so/f8ccd35aeeca4f54b3e02499ded4d795)
    

### BD Dynamo

Estructura Base de Datos

{

user_id: Object(user_id  MD5):

favorite_companies: [

 {

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

}

],

discarded_companies:

[

{

name: string,

created_at: timestamp

},

{

name: string,

created_at: timestamp

}

], 

created_at: timestamp

}

# Lite Version

{

user_id_md5: 

{

favorite_companies: [string, string, string, string, string],

discarded_companies: [string, string, string, string, string],

created_at: timestamp

},

user_id_md5: 

{

favorite_companies: [string, string, string, string, string],

discarded_companies: [string, string, string, string, string],

created_at: timestamp

}

}

##