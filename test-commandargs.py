import sys
from datetime import datetime
from datetime import timedelta

start_date_time = datetime.now()
number_of_minutes = 60

if (len(sys.argv) > 2):
    start_date_string = sys.argv[1]
    start_time_string = sys.argv[2]
    start_date_time_string = start_date_string + " " + start_time_string
    start_date_time = datetime.strptime(start_date_time_string, "%d/%m/%y %H:%M")

if (len(sys.argv) > 3):
    number_of_minutes = int(sys.argv[3])

end_date_time = start_date_time + timedelta(minutes=number_of_minutes)

print start_date_time
print end_date_time
