from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.db.models import Count
from .filters import UserFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.

def get_category_count():
	queryset = models.Property.objects.values('category__title').annotate(Count('category'))	
	return queryset





def Properties_Category_List(request,pk):
	category = models.Category.objects.all()


	category_count = get_category_count()

	most_recent = models.Property.objects.order_by('-timpestamp')[:2]

	model = models.Property.objects.filter(category__pk=int(pk))

	paginator = Paginator(model,3)
	page_var = 'list'
	page = request.GET.get(page_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(page)

	index = paginated_queryset.number - 1 
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]

	
	context = {
		"property":paginated_queryset,
		'page_var':page_var,
		'page_range':page_range,
		'most_recent':most_recent,
		'category_count':category_count,
		'category':category
		}

	template_name = 'properties/properties_category_list.html'	
	return render(request,template_name,context)





def Properties_List(request):
	category = models.Category.objects.all()

	category_count = get_category_count()
	most_recent = models.Property.objects.order_by('-timpestamp')[:2]
	model = models.Property.objects.all()

	

	paginator = Paginator(model,3)
	page_var = 'list'
	page = request.GET.get(page_var)


	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(page)

	index = paginated_queryset.number - 1 
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]

	context = {
		"property":paginated_queryset,
		'page_var':page_var,
		'page_range':page_range,
		'most_recent':most_recent,
		'category_count':category_count,
		'category': category
		}

	template_name = 'properties/properties_list.html'	
	return render(request,template_name,context)	






class Property_detail(generic.DetailView):
	model = models.Property
	template_name = 'properties/property_detail.html'




def search(request):
	model = models.Property.objects.all()
	most_recent = models.Property.objects.order_by('-timpestamp')[:2]
	query1 = request.GET.get('q1')
	query2 = request.GET.get('q2')
	query3 = request.GET.get('q3')
	query4 = request.GET.get('q4')

	paginator = Paginator(model,3)
	page_var = 'list'
	page = request.GET.get(page_var)


	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(page)

	index = paginated_queryset.number - 1 
	max_index = len(paginator.page_range)
	start_index = index - 3 if index >= 3 else 0
	end_index = index + 3 if index <= max_index - 3 else max_index
	page_range = list(paginator.page_range)[start_index:end_index]

	if query1:
		model = model.filter(
				  Q(status__icontains=query1)|
				  Q(address__icontains=query2)|
				  Q(rooms__icontains=query3)| 
				  Q(bathroom__icontains=query4)
				  
				  ).distinct(
				  )
	return render(request,'properties/properties_search_list.html',{'property':paginated_queryset,'page_var':page_var,
		'page_range':page_range,'most_recent':most_recent})

		

	