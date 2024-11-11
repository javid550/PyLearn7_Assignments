print ("------- Test for Tringle -------")

x=float(input("First side : "))
y=float(input("Second side : "))
z=float(input("Third side : "))

if ( x+y>z and y+z>x and x+z>y) :
    print("YES , It's POSSIBLE")

else :
    print("NO , It's IMPOSSIBLE")