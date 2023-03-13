import sqlite3


class Database:

    def __init__(self) -> None:
        self.connection = sqlite3.connect('/home/romcha/projects/qa_auto_23_rch' + '/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        query = "SELECT sqlite_version()"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        print(f"SQLite version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city \
                FROM customers"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        return users

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country \
                FROM customers WHERE name='{name}'"
        self.cursor.execute(query)
        user_address = self.cursor.fetchall()
        return user_address

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products \
                SET quantity={qnt} \
                WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity \
                FROM products \
                WHERE id={product_id}"
        self.cursor.execute(query)
        qnt_product = self.cursor.fetchall()
        return qnt_product

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products \
                WHERE id={product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        join_result = self.cursor.fetchall()
        return join_result

    def get_orders(self):
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        orders = self.cursor.fetchall()
        return orders

    def get_customers(self):
        query = "SELECT * FROM customers"
        self.cursor.execute(query)
        customers = self.cursor.fetchall()
        return customers

    def get_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()
        return products
