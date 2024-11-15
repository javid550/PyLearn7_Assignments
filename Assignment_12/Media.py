import pytube

class Media :

    def __init__(self,type,name,director,score,url,duration,year,casts) :
        self.type = type
        self.name = name
        self.director = director
        self.IMDB_score = score
        self.url = url
        self.duration = duration
        self.production_year = year
        self.casts = casts

    def show_into(self) :
        print () 
        if self.type == "film" :
            print("name \t director \t IMBD_score \t duration \t production year \t casts \t genre")
            print( self.name + "\t" + self.director + "\t" + self.IMDB_score + "\t" + self.duration + "\t" + self.production_year + "\t" + self.casts + "\t" + self.genre)
            print("\n It's a movie . \n")
            print("------------------------------------------------------")

        elif self.type == "series" :
            print("name \t director \t IMBD_score \t production year \t casts \t number of episode")
            print( self.name + "\t" + self.director + "\t" + self.IMDB_score + "\t" + self.production_year + "\t" + self.casts + "\t" + self.episodes_num)
            print("\n It's a series . \n")
            print("------------------------------------------------------")

        elif self.type == "documentary" :
            print("name \t director \t IMBD_score \t duration \t production year")
            print( self.name + "\t" + self.director + "\t" + self.IMDB_score + "\t" + self.duration + "\t" + self.production_year )
            print("\n It's a documentary . \n")
            print("------------------------------------------------------")   

        elif self.type == "clip" :
            print("name \t director \t IMBD_score \t production year \t cast ")
            print( self.name + "\t" + self.director + "\t" + self.IMDB_score + "\t" + self.production_year + "\t" + self.casts )
            print("\n It's a clip . \n")
            print("------------------------------------------------------") 

        else :
            print ("PLZ ask for (Video medias) :/ ")


        def download(self) :
            
            link = self.url
            first_stream = pytube. YouTube(link).streams.first()
            first_stream.download(output_path = './' , file_name="file.mp4")


class Actor :
    def __init__(self , name_of_actor , id) :
        self.id = id
        self.name_of_actor = name_of_actor 