### REQUIRES Requests Library, download here: http://docs.python-requests.org/en/latest/index.html

# Create your views here.
from sail.forms import ControlsForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
import requests
import json

#Controls Sail Movement
def sail(request):
	
	#If we're being POST'ed a form...
	if request.method == 'POST':
		
		#Load the data into a ControlsForm Object
		formdata = ControlsForm(request.POST)
		
		#If the data in the form is valid...
		if formdata.is_valid():
			
			#Get the data from the form
			cd = formdata.cleaned_data
			
			#Construct the URL
			urls = "http://" + cd['server'] + ":" + cd['port'] + "/steer/sail/" + cd['sail']
						
			#Send the Request
			r = requests.get(urls)
			
			#Print the body of the returned HTTP Doc
			print(r.text)
			
			#Make a new form, and render to the user
			moop_ctrl = ControlsForm()
			return render_to_response('sail.html',{'moop': moop_ctrl})
		else:
			#Data isn't valid, show form with error messages
			return render_to_response('sail.html',{'moop': formdata})

	else:
		#If its a GET, then make a new form and render to the user.
		moop_ctrl = ControlsForm()
		return render_to_response('sail.html',{'moop': moop_ctrl})

def info(request):
	
	#Example Info JSON
	body = '{"wind":0.0011397499911254272,"orientation":[0.697615921497345,-0.01157938688993454,-0.023161880671977997],"apr":[39.9704475402832,-0.6634500026702881,-1.3270779848098755],"location":[-4.0831237,52.4140337],"phoneBattery":73}'
	
	#Place the HTTP Request
	result_object = json.loads(body)
	
	#Render the Webpage with the Info Shown
	return render_to_response('info.html',{'location': result_object['location'],
 	'wind': result_object['wind'], 'batt': result_object['phoneBattery'], 
 	'accl':result_object['orientation']})
