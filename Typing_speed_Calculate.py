from time import time
import random as r

def mistake(paraset, usertest):
    error = 0
    for i in range(len(paraset)):
        try:
            if paraset[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

while True:
    ck = input("\nReady to test: yes/no: ")
    if ck == 'yes':
        test = ["If you have gained enough knowledge about the Python programming language and want to get selected by any company", "My name is Zahid Hasan", "I studied in Green university Of Bangladsh"]
        test1 = r.choice(test)
        print("\n**** Typing Speed Test ****")
        print()
        print(test1)
        print()

        time1 = time()
        testinput = input("Enter: ")
        time2 = time()

        print("Speed:", speed_time(time1, time2, testinput), "w/sec")
        print("Error:", mistake(test1, testinput))
    elif ck == 'no':
        print("\nThank You")
        break
    else:
        print("\nWrong Input")
