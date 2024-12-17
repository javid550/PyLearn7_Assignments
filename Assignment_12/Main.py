import pyfiglet

from Media import Media
from Film import Film 
from Series import Series 
from Clip import Clip 
from Documentary import Documentary 
 
  
MEDIA=[] 

def read_dataase() :
    file=open("Data.txt","r") 

    for line in file: 
        res=line.split(",") 
        if len(res) == 10: 
            if res[0] == "film": 
                my_obj = Film(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]) 
            elif res[0] == "series": 
                my_obj = Series(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8]) 
            elif res[0] == "documentary": 
                my_obj = Documentary(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7]) 
            else: 
                my_obj = Clip(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[9]) 
            MEDIA.append(my_obj) 
            
    file.close() 
    
def write_to_database(): 
    data = open("Data.txt", "w") 
    for m in MEDIA: 
        if m.type=="film" or m.type=="documentary": 
            data.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1,---"+"\n") 
        elif m.type=="series": 
            data.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + "," + str(m.episodnumber) + ",---"+"\n") 
        else: 
            data.write(str(m.type)+","+str(m.name)+","+str(m.director)+","+str(m.imdb)+","+str(m.url)+","+str(m.duration)+ "," + str(m.casts) + "," + str(m.productionyear) + ",1," + str(m.genre)+"\n") 
    data.close() 
  
def loading(): 
    result = pyfiglet.figlet_format('your movies', font = 'roman') 
    print(result) 
  
def menu(): 
    print("Enter -1- to Add movie'") 
    print("Enter -2- to Edit movie") 
    print("Enter -3- to Delete movie") 
    print("Enter -4- to Search movie") 
    print("Enter -5- to Show the list of movies") 
    print("Enter -6- to Advance search") 
    print("Enter -7- to Download a movie") 
    print("Enter -8- to Exit") 
  
def add(): 
    type = input("Enter type of media : ") 
    name = input("Enter name of media : ") 
    director = input("Enter director of media : ") 
    imdb = input("Enter IMDB_score of media : ") 
    url = input("Enter url of media : ") 
    duration = input("Enter duration of media : ") 
    casts = input("casts (separate with | ) : ") 
    year = input("production_year : ") 

    if type == "film": 
        genre = input("Enter genre of film : ")
        new_film = Film(type,name,director,imdb,url,duration,casts,year,genre) 
        MEDIA.append(new_film) 
    elif type == "series": 
        episod_num = input("Enter number of episodes of series : ") 
        new_series = Series(type,name,director,imdb,url,duration,casts,year,episod_num) 
        MEDIA.append(new_series) 
    elif type == "documentary": 
        new_documentary = Documentary(type,name,director,imdb,url,duration,casts,year) 
        MEDIA.append(new_documentary) 
    else:  
        new_clip = Clip(type,name,director,imdb,url,duration,casts,year) 
        MEDIA.append(new_clip) 
  
def edit(): 
    name = input("PLZ enter name of media : ") 
  
    for i in range(len(MEDIA)): 
        if MEDIA[i].name == name:     
            print('1 for name') 
            print('2 for IMDB_score') 
            print('3 for casts') 
            print('4 for year') 
            print('5 for duration') 
            print('6 for url') 
            print('7 for exit') 
            selection = int(input("Enter your choice : ")) 

            if selection == 1: 
                MEDIA[i].name = input("reset name : ") 
                print('Done') 
            elif selection == 2: 
                MEDIA[i].IMDB = float(input("reset IMDB_score : ")) 
                print("Done ✅") 
            elif selection == 3: 
                MEDIA[i].casts = input(" reset casts : ") 
                print("Done ✅") 
            elif selection == 4: 
                MEDIA[i].year = int(input("reset year of production : "))
                print("Done ✅") 
            elif selection == 5: 
                MEDIA[i].duration = int(input("reset duration : ")) 
                print("Done ✅") 
            elif selection == 6: 
                MEDIA[i].url = input("reset url : ") 
                print("Done ✅") 
            elif selection == 7: 
                break   
        else: 
            print("NOT Exist ⁉") 
  
def remove(): 
    name = input("Enter the name of movie : ") 
    for media in MEDIA: 
        if media.name == name: 
            MEDIA.remove(media) 
            print("Done ✅") 
            break 
    else: 
        print("Not found!") 
  
def search(): 
    s=input("Enter the name of movie : ") 
    for media in MEDIA: 
        if media.name==s or media.type==s: 
            print(media[media])             
            break 
    else: 
        print("NOT Exist !") 
  
def advanced_search(): 
    min = int(input("minimum minute : ")) 
    max = int(input("maximum minute : ")) 
    n=0 
    for media in MEDIA: 
        if min <= int(media.duration) <= max : 
            media.showinfo() 
            n+=1 
    if n==0: 
        print("NOT Exist !") 
  
def show(): 
    print("name \t   director \t    IMDB \t duration \t\t casts  \t\t year ") 
    print() 
    for media in MEDIA: 
        print(media.name, "\t", media.director, "\t" ,media.imdb, "\t" , media.duration, "\t" , media.casts , "\t" ,media.year) 
        print() 
  
print ("Loading ...⏰ :")
while True: 
    menu() 
    select = int(input("Enter your choice 1 - 8 :")) 
    if  select == 1 : 
        add() 
    elif select == 2: 
        edit() 
    elif select == 3: 
        remove() 
    elif select == 4: 
        search() 
    elif select== 5: 
        show() 
    elif select == 6: 
        advanced_search() 
    elif select == 7: 
        name=input("\n name of movie : ") 
        for m in MEDIA: 
            if m.name==name: 
                m.download() 
    elif select == 8: 
        exit()


