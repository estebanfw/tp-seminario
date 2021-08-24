## Objetivo

Integrar las tecnologías trabajadas durante el seminario intensivo del ITBA:

* Docker
* PostgreSQL
* Una herramienta de visualización: Grafana

La información se levanta via una open api

## Descripción

* Datos de entrada vía [Open API](https://api.coindesk.com/v1/bpi/currentprice.json) de la cotización del bitcoin.
* Se inyecta en una DB de PostgresSQL utilizando linux cronetab para que corra un script de python.
* Se configuran las conexiones de DB y Grafana
* Se crea un dashboard en grafana y se importa a través de un json.

## Ambiente

### Paso 1

Clonar el repo
~~~
git clone https://github.com/estebanfw/tp-seminario
~~~

### Paso 2

Build docker image desde dentro de la carpeta donde fue clonado el repo.
~~~
docker build . -t ubuntu/testing5
~~~
Para verificar si la imagen fue creada se puede correr el siguiente comando y verificar que esté listada.
~~~
docker image ls | grep ubuntu
~~~
Esta imagen de docker ya tiene cargado el script para conectarse a la API, configurada la conexión a la DB de PostgreSQL y configurado el crone con el job
correspondiente para lanzar el script de python cada un minuto. El script de python tiene hardcodeado el localhost, muy probablemente tenga que cambiarlo cada usuario.


### Paso 3

Lanzar ambiente a través del script de bash.

Aclaración de puertos elegidos:
* PostgreSQL: puerto local 5035
* Grafana: puerto local 3030

Para iniciar el ambiente sólo se debe ejecutar.

~~~
chmod +x control.sh
./control.sh start
~~~

### Paso 4 opcional

Chequear que se estén cargando los datos a la db de PostGres
dbname: mydb
user: admin
password: admin
table: btc

Para entrar a la terminal de bash del contenedor se puede utilizar el siguiente comando.
~~~
docker exec -it tp-seminario_db_1 bash
~~~
Dentro de la terminal:
~~~
psql -U admin -d mydb
~~~
Inicia psql y dentro realizar la query:
~~~
select * from btc;
~~~
Un resultado similar a este se debería obtener
~~~
        datetime        |  coin   |   price    
------------------------+---------+------------
 2021-08-24 15:36:00+00 | Bitcoin | 48345.7819
 2021-08-24 15:37:00+00 | Bitcoin | 48507.5392
 2021-08-24 15:38:00+00 | Bitcoin |  48519.984
 2021-08-24 15:39:00+00 | Bitcoin |  48463.819
~~~