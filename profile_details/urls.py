from django.conf.urls import url
from . import views

app_name = "profile_details"

urlpatterns = [

url(r'^property/$',views.Profile_Properties_List,name = "property"),
url(r'^signup/',views.SignUp.as_view(),name = 'signup'),
url(r'^submit/(?P<pk>[-\w]+)/$',views.Submit_Property.as_view(),name = "submit"),
url(r'^update/(?P<pk>[-\w]+)/$',views.Update_Property.as_view(),name = "update"),
url(r'^delete/(?P<pk>[-\w]+)/$',views.Delete_Property.as_view(),name = "delete"),



]