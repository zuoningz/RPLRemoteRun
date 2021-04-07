from django.shortcuts import render
import os
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import requests
import os
from datetime import datetime
from datetime import date
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_POST
def handle_build(request):

	r = requests.get('https://circleci.com/api/v2/pipeline?org-slug=gh/USCRPL',
				 	auth=('a507bc77f71483178f7gjh55b3d39aac1f3bd85', ''))


	if len(r.json()['items'][0]['errors']) == 0:  # if len() == 0, no error, successful build
		# directory to put in my own machine: cd ~/Desktop/RPL/FlightOn \n
		os.system('''
	    	 		  cd ~/RPL/FlightOn \n
	    	 		  git status \n
	                  git pull .
	                   ''')
		#log_to_file('Success')

	# else:
	# 	log_to_file('Failed! ')

	return HttpResponse('') # return a empty HTTP response. code work fine w/o it. add it bc compiler raise error w/o it

		#
		# making local port public for testing webhook

# def log_to_file(status):
# 	file = open('WebhookTestLog.txt', 'a')
# 	today = date.today()
# 	d2 = today.strftime("%B %d, %Y")
# 	now = datetime.now().time()
# 	file.write('Date: ' + str(d2) + '\n')
# 	file.write("Time: " + str(now) + '\n')
# 	file.write(f'Circle CI Build Status: {status} \n\n')
#
# 	file.close()




