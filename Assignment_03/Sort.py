x = []
y = int(input("Enter the number of list : "))

for i in range(y) :
    c = int(input("Your Numbers : "))
    x.append(c)

if sorted(x) == x:
    print("✅")

else :
    print("❌")
