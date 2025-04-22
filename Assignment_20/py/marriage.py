import random

boys = ["ali" , "mahdi" , "reza" , "javad" , "poya" , "hasan"]
girls = ["zahra" , "fati" , "leyli" , "mina" , "sara" , "ziba" , "kobra"]

couples = []


for boy in boys :

    if girls :

        girl = random.choice(girls)
        couples.append((boy , girl))
        girls.remove(girl)
        
    else :
        break

print(couples)