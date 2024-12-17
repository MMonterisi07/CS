import time
import datetime

print ("Mom wakes me up")
current_time = datetime.datetime(2024, 10, 23, 6, 30, 0) 
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    listen = input ("Listen? y/n ").lower()
    if listen == "n":
        print ("Sleep for 5 more minutes")
        time.sleep(2)
        current_time += datetime.timedelta(minutes=5)
        print ("Mom wakes me up")
    elif listen == "y":
        break
        current_time += datetime.timedelta(minutes=1)
    else:
        print("invalid response")
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    m_tue_thur_fri = input ("M,Tue,Thur,Fri? y/n").lower()
    if m_tue_thur_fri == "y":
        print ("Workout clothes")
        break
    elif m_tue_thur_fri == "n":
        while True:
            cold_outside = input ("Cold outside? y/n").lower()
            if cold_outside == "y":
                print ("Cold clothes")
                break
            elif cold_outside == "n":
                print ("Warm clothes")
                break
            else:
                print ("invalid response")
        break
    else:
        print("Invalid response")
print ("walk to bathroom")
print ("brush teeth")
print ("walk down stairs") 
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    breakfast = input ("breakfast? y/n").lower()
    if breakfast == "y":
        print ("sit down at table")
        time.eat(2)
        current_time += datetime.timedelta(minutes=15)
        break
    elif breakfast == "n":
        print ("get cereal")
        time.sleep(2)
        current_time += datetime.timedelta(minutes=15)
        break
    else:
        print ("invalid response")
        break
print ("eat it")
print(current_time.strftime("%H:%M:%S"), end='\r')
while True:
    weekday = input ("weekday? y/n").lower()
    if weekday == "y":
        print ("wet hair and brush it back")
        print ("walk outside")
        print ("play basketball")
        print ("get in car")
        print ("drive to school")
        time.sleep(2)
        current_time += datetime.timedelta(minutes=15)
        print(current_time.strftime("%H:%M:%S"), end='\r')
        gym_day = input ("gym_day? y/n").lower()
        if gym_day == "y":
                print ("walk in gym")
                break
        elif gym_day == "n":
                print ("walk in dining hall")
                break
        else:
                print ("invalid response")
    elif weekday == "n":
        print(current_time.strftime("%H:%M:%S"), end='\r')
        baseball_game = input ("baseball game? y/n").lower()
        if baseball_game == "y":
                print ("put on uniform")
                print ("drive to game")
                time.sleep(2)
                current_time += datetime.timedelta(minutes=60)
                break
        elif baseball_game == "n":
                print ("watch sportscenter")
                break
        else:
                print ("invalid response")
    else:
        print("invalid response")
print(current_time.strftime("%H:%M:%S"), end='\r')


            

            




