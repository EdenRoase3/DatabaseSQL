import sqlite3

#SQL CODE 

CREATE_PRODUCT_TABLES = "CREATE TABLE IF NOT EXISTS market (id INTEGER PRIMARY KEY, name TEXT, shop TEXT, weight REAL, price REAL, shelf TEXT);"

INSERT_PRODUCT = "INSERT INTO market ( name, shop, weight, price, shelf) VALUES(?, ?, ?, ?, ?);"

GET_ALL_PRODUCTS = "SELECT * FROM market;"

GET_PRODUCTS_BY_NAME = "SELECT * FROM market WHERE name = ? ORDER BY name DESC;"

GET_PRICE_FOR_PRODUCT = '''
SELECT * FROM market
WHERE name = ?
ORDER BY weight DESC
LIMIT 1;'''


GET_BY_0_to_100= """
SELECT * FROM market 
WHERE price BETWEEN 0 AND 100   
"""
GET_BY_100_500 = """
SELECT * FROM market 
WHERE price BETWEEN 100 AND 500"""

UPDATE_PRODUCT_NAME = "UPDATE market SET name = ? WHERE name = ?"

UPDATE_PRODUCT_ID = "UPDATE market SET id = ? WHERE name = ?"

DELETE_PRODUCT = "DELETE FROM market WHERE name = ?"

DELETE_BY_ID = "DELETE FROM market WHERE id = ?"

ORDER_BY_PRICE_HIGH = "SELECT price, * FROM market ORDER BY price DESC"

ORDER_BY_PRICE_LOW = "Select price, * FROM market ORDER BY price ASC"

#FUNCTIONS TO ACESS DATABASE

def connect():
        return sqlite3.connect('data.db')
    
    
    #Creating the Database
def create_tables(connection):
        with connection:
            connection.execute(CREATE_PRODUCT_TABLES)
    
    
def add_product(connection,name, shop, weight, price, shelf):
        with connection:
            connection.execute(INSERT_PRODUCT,(name, shop, weight,price,shelf))
    
    
def get_all_products(connection):
        with connection:
            return connection.execute(GET_ALL_PRODUCTS).fetchall()
    
def get_products_by_name(connection,name):
        with connection:
            return connection.execute(GET_PRODUCTS_BY_NAME,(name,))
    
    
def get_price_for_product(connection,name):
        with connection:
            return connection.execute(GET_PRICE_FOR_PRODUCT,(name,)).fetchone()

def get_by_greatthan(connection, price):
    with connection:
        return connection.execute(GET_BY_GREATER_THAN, (price,)).fetchall()

def get_by_lowerthan(connection, price):
    with connection:
        return connection.execute(GET_BY_LOWER_THAN, (price,)).fetchall()

def get_by_range100(connection):
    with connection:
        return connection.execute(GET_BY_0_to_100).fetchall()

def get_by_range100_500(connection):
    with connection:
        return connection.execute(GET_BY_100_500).fetchall()


def update_product_name(connection, name, inputchange):
        with connection: 
            connection.execute(UPDATE_PRODUCT_NAME,[inputchange, name])

            
def update_product_id(connection, name, inputchange):
    with connection:
        connection.execute(UPDATE_PRODUCT_ID, [inputchange, name])
    
def delete_product(connection, name):
        with connection:
            connection.execute(DELETE_PRODUCT,[name,])
            
def delete_by_ID(connection, id):
    with connection: 
        connection.execute(DELETE_BY_ID, [id,])

def order_by_price_hightolow(connection):
    with connection:
        return connection.execute(ORDER_BY_PRICE_HIGH).fetchall()
        
def order_by_price_lowtohigh(connection):
    return connection.execute(ORDER_BY_PRICE_LOW).fetchall()