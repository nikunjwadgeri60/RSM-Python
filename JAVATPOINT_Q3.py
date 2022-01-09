st = int(input('enter speed of train in kmph: '))
st = st * (5 / 18)
print('speed of train is m/s is: ', st)
sl = int(input('length of train is: '))
tt = int(input('time taken by train to cross the bridge: '))
sd = st * tt
print('distance travelled by train to cross the bridge is: ', sd)
lob = sd - sl
print('total length of bridge is: ', lob)
