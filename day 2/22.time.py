import time
print(dir(time))
print(time.time()) #time in seconds since epoch 

print(dir(time))
print(time.localtime()) #time in local time 
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #time in local time in string format