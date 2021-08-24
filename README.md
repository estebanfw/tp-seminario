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