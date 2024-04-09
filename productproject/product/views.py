
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product

class Add_product(CreateView):
    model = Product
    fields = "__all__"


class List_product(ListView):
    model = Product

class Detail_product(DetailView):
    model = Product


class Update_product(UpdateView):
    model = Product

    fields = "__all__"
    success_url = "/"

class Delete_product(DeleteView):
    model = Product
    success_url = "/"
    template_name = "product/Product_confirm.html"
