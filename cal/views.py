from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
import calendar
from . import services

# Create your views here.
def index(request):
	now = datetime.datetime.now()
	month = calendar.month_name[now.month]
	week = services.get_current_week_dates()
	context = {'month': month, 'year': now.year, 'week': week}
	template = loader.get_template('cal/index.html')
	return HttpResponse(template.render(context, request))