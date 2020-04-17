import datetime

def Time_to_Seconds(time):
    return (time.hour * 60 + time.minute) * 60 + time.second

def Get_DateTime(year,month,day,hour,minute,second):
    return datetime.datetime(year, month, day, hour, minute, second)
