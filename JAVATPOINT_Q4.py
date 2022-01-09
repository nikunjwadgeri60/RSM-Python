ts = int(input('enter the train speed in kmph: '))
ts = ts * (5 / 18)
print("train speed in m/s is: ", ts)
tl = int(input('enter length of train: '))
pl = int(input('enter length of platform: '))
distance = tl + pl
print("total distance is: ", distance)
time = (distance / ts)
print("time taken to cross platform is: ", time)
