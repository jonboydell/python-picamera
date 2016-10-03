from datetime import datetime
import time
from picamera import PiCamera

target = datetime(2016, 10, 3, 16, 8)
now = datetime.now()
cont = 1
count = 100

camera = PiCamera()
camera.resolution = (1024, 768)

total_hours = 1
hour_in_minutes = 60
minute_in_seconds = 60
exposures_per_minute = 8

total_exposures = total_hours * hour_in_minutes * minute_in_seconds * exposures_per_minute

while (cont > 0):
    time.sleep(30)
    now = datetime.now()
    print 'no'
    if (now > target):
        print 'yes'
        cont = 0
        for x in range(0, total_exposures):
            print 'photo {0}'.format(x)
            camera.capture('image%s.jpg' % x)
            time.sleep(minute_in_seconds / exposures_per_minute)
