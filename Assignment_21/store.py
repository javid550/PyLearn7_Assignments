import sqlite3

def show_menu() :
    print("1- Add ")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List \n ")
    print("0- Exit")

def load_data_base() :
    global connection
    global my_cursor

    connection = sqlite3.connect("store.db") 
    my_cursor = connection.cursor()

def show_list() :

    result = my_cursor.execute("SELECT * FROM products")

    all_products = result.fetchall()

    for product in all_products :
        print(product)

def add_new() :
    
    products_id = input("Enter the new id :")
    product_name = input("Enter the name of your new product : ")
    product_price = input("Enter the price of your new product : ")
    product_count = input("Enter the number of new product : ")
    my_cursor.execute(f"INSERT INTO products VALUES('{products_id}' , '{product_name}','{product_price}','{product_count}')") 

    # product_price = input("Enter the price of your new product : ")
    # my_cursor.execute(f"INSERT INTO products(price) VALUES('{product_price}')") 

    # product_count = input("Enter the number of new product : ")
    # my_cursor.execute(f"INSERT INTO products(count) VALUES('{product_count}')") 
    connection.commit()

def edit() :
    product_id = input("Enter the ID of that product : ")
    new_price = input("Enter the new price of product : ")
    my_cursor.execute(f"UPDATE products SET price= '{new_price}' WHERE id='{product_id}'")
    connection.commit()

def remove() :
    product_name = input("Enter the products name : ")
    my_cursor.execute(f"DELETE FROM products WHERE name = '{product_name}'")
    connection.commit()

def search() :
    user_product = input("Enter the product name : ")
    result = my_cursor.execute(f"SELECT * FROM products WHERE name = '{user_product}' ")

    product = result.fetchone()

    print(product)


load_data_base()


while True :
    show_menu()
    choice = int(input("Enter your choice : "))

    if choice == 0 :
        exit(0)

    elif choice == 1 :
        add_new()

    elif choice == 2 :
        edit()

    elif choice == 3 :
        remove()
    
    elif choice == 4 :
        search()

    elif choice == 5 :
        show_list()