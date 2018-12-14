import numpy as np
from datetime import datetime

log = open("day4inputtest.txt").read().strip().split("\n")
log = sorted(log)

#print(log)

for line in log:
    dateandtime = line[1:17]
    date, time = dateandtime.split(" ")
    hours, minutes = time.split(":")
    datetime_object = datetime.strptime(date, '%Y-%m-%d').date()
    print(datetime_object)
    print('datetime =', dateandtime, 'date =', date, 'time =', time)
