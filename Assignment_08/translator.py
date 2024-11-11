import gtts

def read_from_flie() :
    global words_bank
    f = open("session 8/translate.txt","r")

    # words =[]
    # for line in f :
    #     words.append(line)

    temp = f.read().split("\n")

    words_bank = []
    for i in range(0 , len(temp) , 2) :
        my_dict = {"ENG" : temp[i] , "PER" : temp[i+1]}
        words_bank.append(my_dict)

        # print(words)

    f.close()

def show_menu() :
    
    print("\n--- welcome to my translator ---")
    print("1_ translate English to Persion ")
    print("2_ translate Persion to English ")
    print("3_ Add a new word to database ")
    print("4_ Exit !!! ")

def english_to_persion() :
    user_text = input("Enter your English text : ")
    user_words = user_text.split(" ")

    for user_word in user_words :
        for word in words_bank :
            if user_word == word["ENG"] :
                print(word["PER"],end = " ")
                break
        else :
            print(user_word,end = " ")

def persion_to_english() :
    user_text = input("Enter your English text : ")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words :
        for word in words_bank :
            if user_word == word["PER"] :
                output = output + word["ENG"] + " "
                # print(word["ENG"],end = " ")
                break
        else :
            output = output + user_word + " "
        print(output)

    x = gtts.gTTS(output , lang="en", slow=False)
    x.save("session 8/voice.mp3")

def add_words() :
    user_ENG_text = input("Enter your English word : ")
    user_PER_text = input("Enter your Persion word : ")
    new_word = {"ENG" : user_ENG_text , "PER" : user_PER_text}
    for word in words_bank :
        if new_word == word :
            print("You had it !!!")
            break
    else:
        words_bank.append(new_word)
        print("+++ The new word added +++")

read_from_flie()

while True :
    show_menu()
    choise = int(input("Enter your choice : "))
    if choise == 1 :
        english_to_persion()
    elif choise == 2 :
        persion_to_english()
    elif choise == 3 :
        add_words()
    elif choise == 4 :
        exit(0)