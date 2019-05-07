from django import forms
from .models import Property

class Property_Form(forms.ModelForm):
	class Meta:
		model = Property
		fields = ('title','status','price','area','rooms','bathroom','address','state','code','images',
		'info','dealer_name','dealer_email','dealer_number','air','parking','swimming','laundry','category',)


		widgets = {
		    'parking': forms.CheckboxInput(attrs={'id':'checkbox1',}),
		    'air': forms.CheckboxInput(attrs={'id':'checkbox2',}),
		    'swimming': forms.CheckboxInput(attrs={'id':'checkbox4',}),
		    'laundry': forms.CheckboxInput(attrs={'id':'checkbox5',}),
		    'title': forms.TextInput(attrs={'class':'input-text',}),
		    'status': forms.Select(attrs={'class':'selectpicker search-fields',}),
		    'price': forms.NumberInput(attrs={'class':'input-text',}),
		    'images': forms.ClearableFileInput(attrs={'class':'custom-file-input',}),
		    'area': forms.TextInput(attrs={'class':'input-text',}),
		    'rooms': forms.Select(attrs={'class':'selectpicker search-fields',}),
		    'bathroom': forms.Select(attrs={'class':'selectpicker search-fields',}),
		    'address': forms.TextInput(attrs={'class':'input-text',}),
		    'state': forms.Select(attrs={'class':'selectpicker search-fields',}),
		    'code': forms.TextInput(attrs={'class':'input-text',}),
		    'info': forms.TextInput(attrs={'class':'input-text','placeholder':'Detailed Information','height':'500px',}),
		    'dealer_name': forms.TextInput(attrs={'class':'input-text','placeholder':'Name'}),
		    'dealer_email': forms.EmailInput(attrs={'class':'input-text','placeholder':'Email Address'}),
		    'dealer_number': forms.TextInput(attrs={'class':'input-text','placeholder':'Phone Number'}),
		    'category': forms.SelectMultiple(attrs={'class':'selectpicker search-fields',}),
	

		}