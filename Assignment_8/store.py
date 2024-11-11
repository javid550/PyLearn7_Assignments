import qrcode 

PRODUCTS = []

def read_from_Data_base() :
    f = open("database.txt","r")

    for line in f :

        result = line.split(",")
        my_dict = {"code" : result[0] , "name" : result[1] , "price" : result[2] , "count" : result[3] }

        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    f = open("database.txt","w")
    for product in PRODUCTS :
        new_product = str(product["code"]) + "," + str(product["name"]) + "," + str(product["price"]) + "," + str(product["count"])

    f.write(new_product)
    f.close()

def show_menu() :
    print("1 : Add")
    print("2 : Edit")
    print("3 : Remove")
    print("4 : Search")
    print("5 : Show")
    print("6 : Buy")
    print("7 : Qr code")
    print("8 : Exit")

def add() :
    code = input("Enter code : ")
    name = input("Enter name : ")
    price = input("Enter price : ")
    count = input("Enter count : ")
    new_products = {"code":code , "name":name , "price":price , "count":count}
    PRODUCTS.append(new_products)

def edit() :
    code = input("Enter code : ")
    
    print("\n","1-name","\n","2-price","\n","3-count")
    your_choice = int(input("Please enter your choice : "))

    for product in PRODUCTS :
        if product["code"] == code :
            if your_choice == 1 :
                product["name"] = input("New name : ")
            elif your_choice == 2 :
                product["price"] = input("New price : ")
            elif your_choice == 3 :
                product["count"] = input("New count : ")
        print("~~~ Informations successfully updated ~~~")
        break
    else :
        print("Not found")

def remove() :
    user_input = input("Enter code : ")

    for product in PRODUCTS :
        if product["code"] == user_input :
            PRODUCTS.remove(product)
            print("~~~ Informations successfully deleted ~~~")
            break
    else : 
        print("not found code") 

def search() :
    user_input = input("Type your keyword : ")
    for product in PRODUCTS :
        if product["code"] == user_input or product["name"] == user_input :
            print(product["code"] , "\t" , product["name"] , "\t" , product["price"])
            break
    else : 
        print("Not Found !!!")

def show_list() :
    print("code\tname\tprice")
    for product in PRODUCTS :
        print(product["code"] , "\t" , product["name"] , "\t" , product["price"])

def buy() :
    while True :

        Entered_code = input("When you're finish enter '0' , Enter code : ")
        if Entered_code != 0 :
            for product in PRODUCTS :
                if product["code"] == Entered_code :
                    count = int(input("How many do need : "))
                    store_count = int(product["count"])

                    if store_count < count :
                        print("Your need is out of range !!! ")
                    else :
                        store_count = store_count - count
                        product["count"] = store_count

                        basket_of_product = {"code":product["code"] , "name":product["name"], "price":product["price"] , "count":product["count"]}
                        products_basket = {}
                        products_basket.append(basket_of_product)

                    break
            else :
                print("--- Not found ---")
        else :
            total = 0
            print("name" , "\t" , "count" , "\t" , "price" )

            for product in products_basket :
                print(product["name"],"\t",product["count"],"\t",product["price"])

                total += (int(product["price"]) * int(product["count"]))
                print("Total : ",total)
                break


def Qrcode() :
    Entered_code = input("Enter code : ")
    for product in PRODUCTS :
        if product["code"] == Entered_code :
            image = qrcode.make("code : " + product["code"] +"\n"+ "name : " + product["name"]  +"\n"+ "price : " + product["price"] +"\n"+ "count : "  + product["count"])
            image.save("QrCode.png")

print("--- Welcome to Javid store ---")
print("Loading . . . ")

read_from_Data_base()
print("Data loaded . ")

while True :
    show_menu()
    choice = int(input("Enter your choice : "))

    if choice == 1 :
        add()
    elif choice == 2 :
        edit()
    elif choice == 3 :
        remove()
    elif choice == 4 :
        search()
    elif choice == 5 :
        show_list()
    elif choice == 6 :
        buy()
    elif choice == 7 :
        Qrcode()
    elif choice == 8 :
        write_to_database()
        exit(0)
    else :
        print("Your choice was out of range !!!")
