from datetime import datetime
import time
import sys
from picamera import PiCamera
from datetime import timedelta

start_date_time = datetime.now()
number_of_minutes = 60
minute_in_seconds = 60
exposures_per_minute = 4

if (len(sys.argv) > 2):
    start_date_string = sys.argv[1]
    start_time_string = sys.argv[2]
    start_date_time_string = start_date_string + " " + start_time_string
    start_date_time = datetime.strptime(start_date_time_string, "%d/%m/%y %H:%M")

if (len(sys.argv) > 3):
    number_of_minutes = int(sys.argv[3])

end_date_time = start_date_time + timedelta(minutes=number_of_minutes)

print 'time is now', datetime.now()
print 'will start at', start_date_time
print 'will end at', end_date_time

camera = PiCamera()
camera.resolution = (1024, 768)

interval = minute_in_seconds / exposures_per_minute
spin = True
x = 0
while (spin):
    now = datetime.now()
    while (now > start_date_time and now < end_date_time):
        print 'shooting'
        x = x + 1
        camera.capture('image%s.jpg' % x)
        print 'waiting', interval
        time.sleep(interval)
        now = datetime.now()
        spin = False
    time.sleep(1)

#target = datetime(2016, 10, 5, 11, 0)
#end_target = datetime(2016, 10, 5, 12, 0)
#now = datetime.now()
#cont = 1
#count = 100

#camera = PiCamera()
#camera.resolution = (1024, 768)

#total_hours = 1
#hour_in_minutes = 60
#minute_in_seconds = 60
#exposures_per_minute = 8
#x = 0

#total_exposures = total_hours * hour_in_minutes * minute_in_seconds * exposures_per_minute

#while (now > target and now < end_target):
#    now = datetime.now()
#    print 'photo {0}'.format(x)
#    camera.capture('image%s.jpg' % x)
#    time.sleep(minute_in_seconds / exposures_per_minute)
#    x = x + 1
