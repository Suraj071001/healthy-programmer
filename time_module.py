from datetime import datetime
start_time = datetime.now().strftime("%M")
print("Start Time is :", start_time)

while True :
    current_time = datetime.now().strftime("%M")
    if int(current_time) - int(start_time) == 1 :
        print("1 min is passed")
        break