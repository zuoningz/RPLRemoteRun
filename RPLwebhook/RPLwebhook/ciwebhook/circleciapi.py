
# Circle CI personal API token: a507bc77f71483178f95f93a5b3d39aac1f3bd85

import requests
import pprint
import os
# r = requests.get('https://circleci.com/api/v2/workflow/39d64ac7-5825-4750-ba13-f7f6061f85d8',
#                  auth=('a507bc77f71483178f95f93a5b3d39aac1f3bd85', '')) # get specific workflow by ID


r = requests.get('https://circleci.com/api/v2/pipeline?org-slug=gh/USCRPL',
                 auth=('a507bc77f71483178f95f93a5b3d39aac1f3bd85', '')) # get all the pipleines of org
# to detect if recent job is successful, check len('errors')
if len(r.json()['items'][0]['errors']) == 0: # if len() == 0, no error, successful build
    os.system('''
    	 		  cd ~/Desktop/RPL/FlightOn \n
    	 		  git status \n
                  git pull .
                   ''')


pprint.pprint(r.json())


