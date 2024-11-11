print("----- Check up for your health -----")

x = float(input("Enter your weight in Kilogram : "))
y = float(input("Enter your height in Meter : ")) 

BMI = x/y**2

print ("Body Mass Index : " , BMI)

if (BMI < 18.5) :
    print (" Underweight !!! ")

elif (18.5 < BMI < 24.9) :
    print (" Normal Weight ")

elif (25 < BMI < 29.9):
    print (" Overweight ! ")

elif (30 < BMI < 34.9):
    print (" Obesity !! ")

elif (35 < BMI < 39.9):
    print (" Extreme Obesity !!! ")
