a = input("Enter your numbers & separate them with ',' : ")

values = a.split(',')

arr = []

for i in values :
     
    clean_value = i.strip()

    numbers = int(clean_value)

    arr.append(numbers)

def symmetric(arr) :
        
        return arr == arr[::-1]

result = symmetric(arr)

if result : 
    print(f"Yes {arr} is symmetric")
    
else : 
    print(f"No {arr} isn't symmetric")