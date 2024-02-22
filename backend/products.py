import mysql.connector

cnx = mysql.connector.connect(user='root', password='Varma',
                              host='127.0.0.1',
                              database='gs.products')
cursor = cnx.cursor()

query = ("select * from gs.products")

for (product_id, name, units_of_measure_id, price_per_unit) in cursor:
    print(product_id, name, units_of_measure_id, price_per_unit)

cnx.close()

