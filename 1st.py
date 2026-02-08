import mysql.connector

connection = mysql.connector.connect(

    port=3306,
    host='127.0.0.1',
    user="yashmaya",
    pasword="yashmayaa",
    database="flight_game",
    autocommit=True)

cursor = connection.cursor()