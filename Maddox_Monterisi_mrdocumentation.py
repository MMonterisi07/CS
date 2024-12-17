import time
import datetime

print ("Mom wakes me up")                                           #displays message 
current_time = datetime.datetime(2024, 10, 23, 6, 30, 0)            #sets current time
print(current_time.strftime("%H:%M:%S"), end='\r')                  #displays current time in hours, minutes, seconds
while True:                                                         #forever loop
    listen = input ("Listen? y/n ").lower()                         #stores user response in variable listen
    if listen == "n":                                               #if the user does not listen
        print ("Sleep for 5 more minutes")                          #displays message
        time.sleep(2)                                               #stops time for 2 seconds
        current_time += datetime.timedelta(minutes=5)               #adds five minutes to the time
        print ("Mom wakes me up")                                   #displays message
    elif listen == "y":                                             #if the user listens
        break                                                       #stops forever loop
        current_time += datetime.timedelta(minutes=1)               #adds 1 minute to current time
    else:                                                           #if the user inputs something else
        print("invalid response")                                   #displays message
print(current_time.strftime("%H:%M:%S"), end='\r')                  #displays current time in hours, minutes, seconds
while True:                                                         #forever loop
    m_tue_thur_fri = input ("M,Tue,Thur,Fri? y/n").lower()          #stores user response in variable M,Tue,Thur,Fri
    if m_tue_thur_fri == "y":                                       #if it is M,Tue,Thur,Fri
        print ("Workout clothes")                                   #displays message
        break                                                       #stops forever loop
    elif m_tue_thur_fri == "n":                                     #if it is not M,Tue,Thur,Fri
        while True:                                                 #forever loop
            cold_outside = input ("Cold outside? y/n").lower()      #stores user response in variable cold outside
            if cold_outside == "y":                                 #if it is cold outside
                print ("Cold clothes")                              #displays message
                break                                               #stops forever loop
            elif cold_outside == "n":                               #if it is not cold outside
                print ("Warm clothes")                              #displays message
                break                                               #stops forever loop
            else:                                                   #if user inputs something else
                print ("invalid response")                          #displays message
        break                                                       #stops forever loop
    else:                                                           #if user imputs something else
        print("Invalid response")                                   #displays message
print ("walk to bathroom")                                          #displays message
print ("brush teeth")                                               #displays message 
print ("walk down stairs")                                          #displays message
print(current_time.strftime("%H:%M:%S"), end='\r')                  #displays current time in hours, minutes, seconds
while True:                                                         #forever loop
    breakfast = input ("breakfast? y/n").lower()                    #stores user response in variable breakfast
    if breakfast == "y":                                            #if breakfast is ready
        print ("sit down at table")                                 #displays message
        time.sleep(2)                                               #stops time for 2 seconds
        current_time += datetime.timedelta(minutes=15)              #adds 15 minutes to the current time
        break                                                       #stops forever loop
    elif breakfast == "n":                                          #is breakfast is not ready                       
        print ("get cereal")                                        #displays message
        time.sleep(2)                                               #stops time for 2 seconds
        current_time += datetime.timedelta(minutes=15)              #adds 15 minutes to the current time
        break                                                       #stops forever loop
    else:                                                           #if user inputs something else
        print ("invalid response")                                  #displays message
        break                                                       #stops forever loop
print ("eat it")                                                    #displays message
print(current_time.strftime("%H:%M:%S"), end='\r')                  #displays current time in hours, minutes, seconds
while True:                                                         #forever loop
    weekday = input ("weekday? y/n").lower()                        #stores user response in variable weekday
    if weekday == "y":                                              #if it is a weekday
        print ("wet hair and brush it back")                        #displays message
        print ("walk outside")                                      #displays message
        print ("play basketball")                                   #displays message
        print ("get in car")                                        #displays message
        print ("drive to school")                                   #displays message
        time.sleep(2)                                               #stops time for 2 seconds
        current_time += datetime.timedelta(minutes=15)              #adds 15 minutes to current time
        print(current_time.strftime("%H:%M:%S"), end='\r')          #displays current time in hours, minutes, seconds
        gym_day = input ("gym_day? y/n").lower()                    #stores user response in variable gym day 
        if gym_day == "y":                                          #if it is a gym day
                print ("walk in gym")                               #displays message
                break                                               #stops forever loop
        elif gym_day == "n":                                        #if it is not a gym day
                print ("walk in dining hall")                       #displays message
                break                                               #stops forever loop
        else:                                                       #if user inputs something else
                print ("invalid response")                          #displays message
    elif weekday == "n":                                            #if it is not a weekday
        print(current_time.strftime("%H:%M:%S"), end='\r')          #displays current time in hours, minutes, seconds
        baseball_game = input ("baseball game? y/n").lower()        #stores user response in variable baseball game
        if baseball_game == "y":                                    #if there is a baseball game
                print ("put on uniform")                            #displays message
                print ("drive to game")                             #displays message
                time.sleep(2)                                       #stops time for 2 seconds
                current_time += datetime.timedelta(minutes=60)      #adds 60 minutes to current time
                break                                               #stops forever loop
        elif baseball_game == "n":                                  #if there is not a baseball game
                print ("watch sportscenter")                        #displays message
                break                                               #stops forever loop
        else:                                                       #if user inputs something else
                print ("invalid response")                          #displays message
    else:                                                           #if user inputs something else
        print("invalid response")                                   #displays message
print(current_time.strftime("%H:%M:%S"), end='\r')                  #displays current time in hours, minutes, seconds


            

            




