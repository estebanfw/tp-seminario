import requests, json
import psycopg2
import datetime as dt

URL="https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url=URL)
data=r.json()
print("Request done to {} at ".format(URL,dt.datetime.now()))
print("-------------------------------------------------------------------------")
print("Request Output")
print(r.json())

time=data.get("time").get("updatedISO")
cryptocoin=data.get("chartName")
usdprice=data.get("bpi").get("USD").get("rate_float")

try:
    connection = psycopg2.connect(user="admin",
                                  password="admin",
                                  host="192.168.1.8",
                                  port="5435",
                                  database="mydb")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO btc (datetime, coin, price) VALUES (%s,%s,%s)"""
    record_to_insert = (time, cryptocoin, usdprice)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into btc table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into btc table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")