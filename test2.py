

import datetime
import locale
date_time_str = 'Jun 28 2018 7:40AM'
date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

date_time_str = '23.05.2021'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d.%m.%Y')

strd = str(date_time_obj)

year = strd[:4]
month = strd[5:7]
day = strd[8:10]

print(day + "." + month + "." + year)

endDate = date_time_obj + datetime.timedelta(days = 1)


print('Date:', date_time_obj.date())

print('Date:', endDate.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)
