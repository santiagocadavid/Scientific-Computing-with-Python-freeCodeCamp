def add_time(start, duration, day=None):

    days = ['Monday', 'Tuesday' , 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    

    #Start information
    Initial_info = start.split(":")
    Initial_info_schedule = start.split(" ")
    #Hour
    Initial_hour = int(Initial_info[0]) 
    #Minutes
    Initial_minutes = int(Initial_info[1][:2])
    #Day
    if day:
        day = day.lower().capitalize()    
        num_day = days.index(day)


    #Schedule of the day
    schedule = Initial_info_schedule[1]
    
    #Next information
    Duration_info = duration.split(":")
    Next_hour = int(Duration_info[0])
    Next_minutes = int(Duration_info[1])
    
    Extrahours = 0
    Extradays = 0


    Final_minutes = Initial_minutes + Next_minutes

    #Final_minutes>60? --> Calculate extra hours
    if Final_minutes>60:
        Extrahours += int(Final_minutes/60)      #Hours  
        Final_minutes = int(Final_minutes%60)    #Minutes


    if Final_minutes<10:
        Final_minutes = "0" + str(Final_minutes)

    Final_hours = int(Initial_hour) + Next_hour + Extrahours
    
    #Final_hours>24? --> Calculate extra days
    if Final_hours>24:
        Extradays = int(Final_hours/24)      
        Final_hours = int(Final_hours%24)    
    
    
    #Day schedule AM or PM
    if schedule == 'AM':
        if Final_hours>12:
            Final_hours = Final_hours - 12
            
            schedule = 'PM'

        elif Final_hours==12:
            
            schedule = 'PM'

        elif Final_hours<12:
            schedule = 'AM'

            
    elif schedule == 'PM':
        if  Final_hours<1:
            
            Final_hours = 12
            schedule = 'AM'
            
        elif Final_hours>12:
            Extradays +=1
            Final_hours = Final_hours - 12
            schedule = 'AM'
        
        elif Final_hours==12:
            Extradays +=1
            schedule = 'AM'

    

    if day:
        #Days later
        day = days[int((num_day + Extradays)%7)]

        if Extradays==1:
            
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule + ", " + day + " (" + "next day" + ")" 
        
        elif Extradays>1:
            
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule + ", " + day + " (" + str(Extradays) + " days " + "later" + ")" 

        else:
            
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule + ", " + day
    
    else:

        #Days later
        if Extradays==1:
            #print(Extradays)
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule  + " (" + "next day" + ")" 
        
        elif Extradays>1:
            #print(Extradays)
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule + " (" + str(Extradays) + " days " + "later" + ")" 

        else:
            #print(Extradays)
            new_time = str(Final_hours) + ":" + str(Final_minutes) + " " + schedule 


    return(new_time)