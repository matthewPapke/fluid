from datetime import datetime, timedelta
import calendar

def get_current_week_dates():
	week = {}
	# day_num = datetime.datetime.now().weekday()
	# day_name: calendar.day_name[day_num]
	# date = datetime.now().day
	# week[day_name] = date
	
	# get week's days
	for i in range(7):
		day = (datetime.now()- timedelta(i))
		day_name = calendar.day_name[day.weekday()]
		week[day_name] = day.day
			
	return week
