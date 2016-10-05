from datetime import datetime
import time
from picamera import PiCamera

target = datetime(2016, 10, 3, 11, 0)
end_target = datetime(2016, 10, 5, 12, 0)
now = datetime.now()
cont = 1
count = 100

camera = PiCamera()
camera.resolution = (1024, 768)

total_hours = 1
hour_in_minutes = 60
minute_in_seconds = 60
exposures_per_minute = 8
x = 0

total_exposures = total_hours * hour_in_minutes * minute_in_seconds * exposures_per_minute

while (now > target && now < end_target):
    now = datetime.now()
    print 'photo {0}'.format(x)
    camera.capture('image%s.jpg' % x)
    time.sleep(minute_in_seconds / exposures_per_minute)
    x = x + 1
