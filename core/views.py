from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto

# Read

class IndexViews(ListView):
    model = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'

# Create

class CreateProdutoViews(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

# Update

class UpdateProdutoViews(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

# Delete

class DeleteProdutoViwes(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')



