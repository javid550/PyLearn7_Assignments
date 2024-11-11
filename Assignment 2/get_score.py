print ("Welcome to calculator of your average")
print("When you are finish , Enter 'exit' ")
scores_sum = 0.0
number_of_scores= 0
while True:

    score = input("score of your lesson : ")

    if score == "exit" :
        break
    
    score = float(score)
    scores_sum = scores_sum + score
    number_of_scores = number_of_scores + 1

avg = scores_sum / number_of_scores

print ("Average : ", avg )
