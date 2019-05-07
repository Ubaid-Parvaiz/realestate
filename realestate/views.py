from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import redirect
from properties import models

def Home(request):
	most_recent = models.Property.objects.order_by('-timpestamp')[:6]

	template_name = 'index.html'

	return render(request,template_name,{'most_recent':most_recent})

def About(request):
	

	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		number = request.POST.get('phone')
		subject_sender = request.POST.get('subject')
		message = request.POST.get('message')

		subject = 'Message from ubaidparvaiz.com recieved'
		from_email = email
		to_email = [settings.DEFAULT_FROM_EMAIL]
		context = {'user':name,
				   'email':email,
				   'message':message,
				   'subject_sender':subject_sender,
				   'number':number
				   }

		
		contact_message = get_template('contact_message.txt',).render(context)

		send_mail(subject,contact_message,from_email,to_email,fail_silently = True)

		return redirect('success')

	return render(request,'about.html')	
		

def success(request):
	return render(request,'success.html')