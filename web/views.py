from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from . models import Product
# Create your views here.
# class based

class IndexView(TemplateView):
    template_name='web/index.html'
   
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["produ"] = Product.objects.all()
        return context

class ProductDetails(DetailView):
    template_name='web/details.html'
    model=Product
    


