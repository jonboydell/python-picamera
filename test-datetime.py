from datetime import datetime
import time
from picamera import PiCamera

target = datetime(2016, 10, 3, 14, 00)
now = datetime.now()
cont = 1
count = 100

camera = PiCamera()

while (cont > 0):
    time.sleep(30)
    now = datetime.now()
    print 'no'
    if (now > target):
        print 'yes'
        cont = 0
        for x in range(0, count):
            print 'photo {0}'.format(x)
            camera.capture('image%s.jpg' % x)

            time.sleep(30)
