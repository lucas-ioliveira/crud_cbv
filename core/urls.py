from django.urls import path
from .views import IndexViews, CreateProdutoViews, UpdateProdutoViews, DeleteProdutoViwes

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('add/', CreateProdutoViews.as_view(), name='add_produto'),
    path('<int:pk>/update', UpdateProdutoViews.as_view(), name='upd_produto'),
    path('<int:pk>/delete', DeleteProdutoViwes.as_view(), name='del_produto'),
]