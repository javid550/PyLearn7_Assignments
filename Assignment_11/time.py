class Time :
    def __init__(self , hour , minute , second) :
        # print("This is init method")
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()


    def show(self) :
        print(self.hour , ":" , self.minute , ":" , self.second)

    def sum(self , other) :
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new , m_new , s_new)
        return result
    
    def sub(self , other) :
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new , m_new , s_new)
        return result
    
    def fix(self) :
        if self.second >= 60 :
            self.second -= 60
            self.minute += 1

        if self.minute >= 60 :
            self.minute -= 60
            self.hour += 1
        
        if self.second < 0 :
            self.second += 60
            self.minute -= 1

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1

    def Time_to_Sec(self) :
        self.sec_Time = self.second + self.minute*60 + self.hour*3600
        return self.sec_Time

    def Sec_to_Time(self , second):
        hour = second // 3600 
        minute = (second % 3600) // 60 
        seconds = second % 60

        Sec_Time = Time(hour,minute,seconds)
        # return Sec_Time
        # self.fix()
        Sec_Time.show()
        


    def convert(self , t) :
        new_time = self.sum(t)
        return new_time 


T1 = Time(3 , 75 , 17)
T1.show() 

print(T1.Time_to_Sec())

T2 = Time(5 , 35 , 20)
T2.Sec_to_Time(15437)

T3 = Time(5 , 13 , 2)
T3.show()

T4 = T1.sum(T2)
T4.show()

tehran_city = Time(5,30,40)
T5 = T4.convert(tehran_city)
T5.show()