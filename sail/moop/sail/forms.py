#Create Forms Here
from django import forms
from django.forms import *
from django.forms.util import ErrorList
from django.contrib.auth.models import User

class ControlsForm(forms.Form):
	server = CharField(max_length=100, required=True)
	port = 	CharField(max_length=250, required=True)
	sail = 	CharField(max_length=250, required=True)

	def clean(self):
		cleaned_data = self.cleaned_data

		srv = cleaned_data.get('server')
		prt = cleaned_data.get('port')
		sailpos = cleaned_data.get('sail')

		if srv == None:
			self._errors['server'] = ErrorList(["Please Server Address"])
		if prt == None:
			self._errors['port'] = ErrorList(["Please Server Port"])
		if sailpos == None:
			self._errors['sail'] = ErrorList(["Please Sail Angle"])
		
		return cleaned_data
