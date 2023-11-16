from django.contrib import admin
from django.urls import path,include
from .views import IndexView,ProductDetails

# it need for class based view
app_name='web'

urlpatterns = [
 
    path("",IndexView.as_view(),name='index'),
    path("details/<int:pk>",ProductDetails.as_view(),name='details')
]
