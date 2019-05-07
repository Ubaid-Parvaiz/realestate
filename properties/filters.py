import django_filters
from . import models

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = models.Property
		fields = ['status','state','rooms','bathroom','area','price']