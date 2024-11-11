seconds = int(input("Enter Seconds : ")) 

H = seconds // 3600
temp = (seconds - H*3600)
M = temp // 60
S = temp - ( M*60 )

print("Time : " , H ,":", M , ":" , S)