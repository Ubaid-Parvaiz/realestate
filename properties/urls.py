from django.conf.urls import url
from . import views

app_name = 'property'

urlpatterns = [


url(r'^list/$',views.Properties_List,name = "list"),

url(r'^search/$',views.search,name = "search"),

url(r'^category/(?P<pk>[-\w]+)/$',views.Properties_Category_List,name = "category"),

url(r'^detail/(?P<pk>[-\w]+)/$',views.Property_detail.as_view(),name = "detail"),

]