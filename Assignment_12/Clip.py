from Media import media

class Clip(media) :
    def __init__(self,type,name,director,IMDB_score,url,duration,casts,country) :
        super().__init__(type,name,director,IMDB_score,url,duration,casts) 
        self.country = country