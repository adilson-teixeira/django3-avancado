from django.urls import path

from .views import produto, IndexView #index, 
#app_name = 'django3'

urlpatterns = [
    path('', IndexView.as_view(),name='index'), #class based Views
    #path('', index, name='index'),
    path('produto/', produto, name='produto'), #Function based Views
    
]

