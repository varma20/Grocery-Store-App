from connection import sql_connection

def get_all_products(connection):

    cursor = connection.cursor()

    query = "select * from gs.products"
    cursor.execute(query)

    response = []
    for (product_id, name, units_of_measure_id, price_per_unit) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name':name,
                'unit_of_measure_id': units_of_measure_id,
                'price_per_unit':price_per_unit
            }
        )

    connection.close()
    return response

def insert_a_product(connection,product):
    cursor = connection.cursor()

    query = ("INSERT INTO products""(name, units_of_measure_id, price_per_unit)""VALUES (%s,%s,%s)")
    
    data = (product['product_name'],product['units_of_measure_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_a_row(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()


if __name__ == "__main__":
    connection = sql_connection()
    print(delete_a_row(connection,5))