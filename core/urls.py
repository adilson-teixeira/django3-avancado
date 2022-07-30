from django.urls import path

from .views import CarIndexView, produto, IndexView, CarIndexView, CreateCarroView, UpdateCarroView, DeleteCarroView #index, 
#app_name = 'django3'

urlpatterns = [
    path('', IndexView.as_view(),name='index'), #class based Views
    path('carindex/', CarIndexView.as_view(), name='carindex'),
    path('add/', CreateCarroView.as_view(), name='add_carro'),
    path('<int:pk>/update/', UpdateCarroView.as_view(), name='upd_carro'),
    path('<int:pk>/delete/', DeleteCarroView.as_view(), name='del_carro'),
    #path('', index, name='index'),
    path('produto/', produto, name='produto'), #Function based Views
    
]

