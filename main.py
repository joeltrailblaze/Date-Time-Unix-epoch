from datetime import datetime

# DATE TO SECONDS
def DTS(date:str,hours:int=00,minute:int=00,second=0,microsecond=0)->None:
     """
     DTS: Date To Seconds, This Function is used to convert Date to Seconds Format
     """
     year = date[:4]
     month = date[4:6]
     day = date[6:]
     seconds = datetime(int(year),int(month),int(day),hours,minute,second,microsecond,tzinfo=None)
     return seconds.timestamp()

# SECONDS TO DATE
def STD(seconds:int)->None:
     """
     STD: Seconds To Date, This Function is used to convert Seconds To Date Format
     """
     a = datetime.fromtimestamp(seconds)
     return a

#GET DIGIT COUNT
def GDC(seconds:int)->None:
     """
     GDC: Get Digit Count, This Function is used to get the number of digit present in seconds...
     """
     a = str(seconds)
     itr:int = 0
     for i in a:
          itr = itr + 1
     return itr

