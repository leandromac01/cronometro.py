import time
i = 1
second = 0
minute = 0
hour = 0
ct_sec = ""
ct_min = ""
ct_hour = ""
while i == 1:
    for looping in range(i):
        time.sleep(1)
        second+=1
        if (second>=60):
            second=0
            minute+=1
        if (minute >=60):
            minute=0
            hour+=1
        if (second <=9):
            ct_sec = "0%s"
        else:
            ct_sec = "%s"
        if (minute <=9):
            ct_min = "0%s"
        else:
            ct_min = "%s"
        if (hour <=9):
            ct_hour = "0%s"
        else:
            ct_hour = "%s"
        print((ct_hour+":"+ct_min+":"+ct_sec) % (hour, minute, second))
        # Created by Leandro Macedo - 2023