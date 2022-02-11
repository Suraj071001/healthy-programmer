from datetime import datetime
from pygame import mixer
from time import sleep

# Starting the mixer
mixer.init()

#loading the song
mixer.music.load("heymama.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

start_time = datetime.now().strftime("%H:%M:%S")
st_time = int(datetime.now().strftime("%H"))
print(start_time)

def check_log(log) :
    if log == "1" :
        with open("water_log.txt") as w :
            print(w.readlines())
    elif log == "2" :
        with open("exercise_log.txt") as e :
            print(e.readlines())
    elif log == "3" :
        with open("eyes_exercise_log.txt") as ey :
            print(ey.readlines())
    elif log == "c":
        print("thanks for continue ,now i help you to stay healthy :")
    else :
        print("Please enter \n'1' for water_log \n'2' for exercise_log\n'3' for eyes_log\n'c' for continue \n")
while True :
    log1 = input("Enter '1' for water_log \t'2' for exercise_log\t'3' for eyes_log\tor\t'c' for continue :")
    check_log(log1)
    if log1 == "c" :
        break

while True :
    current_time = int(datetime.now().strftime("%M%S"))
    cu_time = int(datetime.now().strftime("%H"))
    hr_pass = cu_time - st_time

    #time to drink water
    if current_time==2000 or current_time==4000 or current_time==0000:
        # Start playing the song
        mixer.music.play()
        w_log = datetime.now().strftime("%H:%M:%S")
        a = input("Enter 'done' if you drank water :")
        if a == "done" :
            mixer.music.stop()
            print(w_log)
            with open("water_log.txt","a") as w :
                w.write(f"drink water at :{w_log} \n")
            continue
        elif a != "done":
            mixer.music.stop()

            with open("water_log.txt","a") as w :
                w.write(f"Forget to drink water at :{w_log}\n")
            continue

    elif current_time==4500 or current_time==1500 :
        mixer.music.unload()
        mixer.music.load("belly_dancer.mp3")
        mixer.music.play()
        e_log = datetime.now().strftime("%H:%M:%S")
        b = input("Enter 'exdone' or 'done' if you done your exercise :")
        if b == "exdone" or "done" :
            mixer.music.stop()
            with open("exercise_log.txt","a") as e :
                e.write(f"Exercise done at :{e_log}\n")
            continue
        elif b != "exdone" or "done" :
            mixer.music.stop()
            with open("exercise_log.txt","a") as e :
                e.write(f"Forget to done exercise at :{e_log}\n")
            continue

    elif current_time==3000 or current_time== 500 :
        mixer.music.load("barso_re.mp3")
        mixer.music.play()
        ey_log = datetime.now().strftime("%H:%M:%S")
        c = input("Enter 'eydone' or 'done' if you done eyes exercises :")
        if c == "eydone" or "done" :
            mixer.music.stop()
            with open("eyes_exercise_log.txt","a") as ey :
                ey.write(f"Eyes exercise done at :{ey_log}\n")
            continue
        elif c != "eydone" or "done" :
            mixer.music.stop()
            with open("eyes_exercise_log.txt","a") as ey :
                ey.write(f"Forget to done eyes exercise at :{ey_log}\n")
            continue

    elif hr_pass == 7 :
        break
