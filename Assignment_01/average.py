print ("Welcome to calculator of your average")
input ("Enter your first name PLZ : ")
input ("Enter your last name PLZ : ")

a = float(input("score of first lesson : "))
b = float(input("score of second lesson : "))
c = float(input("score of third lesson : "))

avg = (a+b+c)/3
print ("average : ", avg )

if (avg >= 17) :
    print ("Excellent ; you're in Top")

elif (17 > avg >= 12):
    print ("Normal ; you can be better")

elif (avg < 12):
    print ("FAIL , Sorrrrry !!!")

else :
    print ("PLEASE , Enter your score between 0-20 ")