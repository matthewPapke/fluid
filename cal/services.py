from datetime import datetime, timedelta
import calendar

def get_current_week_dates():
	week = {}	
	# get week's days
	for i in range(7):
		day = (datetime.now()- timedelta(i))
		day_name = calendar.day_name[day.weekday()]
		week[day_name] = day.day
			
	return week
