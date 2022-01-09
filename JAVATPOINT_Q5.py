tl = int(input('enter the train length: '))
st = int(input('enter speed of train in kmph: '))
sm = int(input('enter speed of man in kmph: '))
rs = (st - sm)
print('relative speed in kmph is: ', rs)
rs = (rs * (5 / 18))
print('relative speed in m/s is: ', rs)
time = tl / rs
print('time taken by train to cross man is: 1', time)
