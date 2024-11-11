def check_board(row,culomn) :

    for j in range(culomn):
        for i in range(row) :
            if ( j+i ) % 2 == 0 :
                print('*',end="")
            else :
                print('#',end="")
        print( )

row = int(input("Enter a number : "))
culomn = int(input("Enter another number : "))

check_board(row,culomn)