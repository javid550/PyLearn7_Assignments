def Mul_table(row,culomn) :

    for j in range(1 , culomn + 1):
        for i in range(1 , row + 1) :
            print( f"{i*j : 4}",end="" )
        print( )

row = int(input("Enter a number : "))
culomn = int(input("Enter another number : "))

Mul_table(row,culomn)