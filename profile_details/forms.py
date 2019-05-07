from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password')
		
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}),
			'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'passowrd'}),
			}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for fieldname in ['username']:
			self.fields[fieldname].help_text = None


		



