from django.shortcuts import render
from django.views import generic 
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from properties import models
from properties import forms
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def Profile_Properties_List(request):
	properties = models.Property.objects.filter(user=request.user)
	return render(request, 'profile_details/my-properties.html', {'property': properties})

	
class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'profile_details/signup.html'



class Submit_Property(generic.CreateView,LoginRequiredMixin):
	model = models.Property
	form_class = forms.Property_Form
	template_name = 'profile_details/submit-property.html'
	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super().form_valid(form)





class Update_Property(generic.UpdateView,LoginRequiredMixin):
	model = models.Property
	form_class = forms.Property_Form
	template_name = 'profile_details/submit-property.html'

class Delete_Property(generic.DeleteView,LoginRequiredMixin):
	model = models.Property
	form_class = forms.Property_Form
	template_name = 'profile_details/delete-property.html'
		
	def get_success_url(self, **kwargs):
	# obj = form.instance or self.object
		return reverse_lazy("profile_details:property", kwargs={'pk': self.object.pk})

