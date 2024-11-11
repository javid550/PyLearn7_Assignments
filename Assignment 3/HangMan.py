import random

words_bank = ["tree" , "fish" , "workout" , "butterfly" , "cute" , "dog" , "star" , "sky"]
user_mistake = 0

x = random.randint(0 , len(words_bank)-1)

word = words_bank[x]

correct_chars = []
wrong_chars = []

# word = random.choice(words_bank)
# print(word)

while user_mistake < 6 :

    for i in range (len(word)):
        if word[i] in correct_chars :
            print(word[i] , end=" " )
        else :
            print(" _ " , end=" " )

    if  len(correct_chars) != (len(word)) :

        user_char = input("please write your guess : ").lower()
        if len(user_char) == 1 :

            if  user_char in word :
                correct_chars.append(user_char)
                print("✅")
            else :
                wrong_chars.append(user_char)
                user_mistake += 1
                print("❌")
        else :
            print("please enter one charector")

    else :
        print("--- YOU WIN ---")
        break

if user_mistake == 6 :
    print("Game Over ☠")

else :
    print("--- YOU WIN ---")