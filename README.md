# FlightOnRemoteRun
Remote runner for FlightOn.


code to do "git pull" every time Circle CI has successful build. 
This code is still developing and I will work on simplying it. 
There is added functionalities in this code to open a file called 
WebhookTestLog.txt to document wether each build is successful. 
To disable this functionality, comment out the two calls to 
log_to_file('Success')
log_to_file('Failed!')
in line 26 and 29 in RPLwebhook/ciwebhook/views.py file