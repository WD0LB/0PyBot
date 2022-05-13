    #Calendar.py
#Youness & Walid
#Essential target: create a GUI Calendar with basic functionalities
#Compliment target: integrate Calendar with 0PyBot voice functinality

#rules bro: comments comments comments :)
#brthday: pop up
#tasks day, create delete
#content to text => voice
#api google supp ;)
#
#______________________________________________________
#1ST TARGET: GUI CALENDAR
import calendar
yy = 2022
mm = 5
print(calendar.calendar(yy, 2, 1, 6))
print(calendar.month(yy,mm))

text_cal = calendar.HTMLCalendar(firstweekday = 0)

year = 2018
month = 9
# default value of width is 0

# printing formatmonth
print(text_cal.formatmonth(year, month))
i = open('index.html', 'w')
i.write(str(text_cal.formatmonth(year, month)))
i.close()

import os
os.system('open index.html')
#google calendar api
#https://www.youtube.com/playlist?list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on
