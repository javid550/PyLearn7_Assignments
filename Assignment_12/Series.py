from Media import Media

class Series(Media) :
    def __init__(self,type,name,director,IMDB_score,url,duration,casts,episodes_num) :
        super().__init__(type,name,director,IMDB_score,url,duration,casts) 
        self.episodes_num = episodes_num