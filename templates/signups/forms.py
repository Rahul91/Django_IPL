from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import ipl_scores
from django.contrib import auth

class customizedform(UserCreationForm):
	#Email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
	
	def save(self, commit = True):
		user = super(UserCreationForm, self).save(commit=False)
		#user.Email = self.cleaned_data['Email']
		#user.username = self['username']	#user.username = None
		#user.password = self['password1']
		#user.username = self['username']
		if commit:
			user.save()

		return user

'''
class ipl_scores(forms.ModelForm):

	class Meta:
		model = ipl_scores
		fields = ('Detail', 'Score1', 'Score2')
		'''