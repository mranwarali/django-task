from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Stock, Order, StockTransfer

# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'sku', 'description', 'price']
    template_name = 'inventory/product_form.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'sku', 'description', 'price']
    template_name = 'inventory/product_form.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = '/products/'

# Stock views
class StockListView(ListView):
    model = Stock
    template_name = 'inventory/stock_list.html'

class StockDetailView(DetailView):
    model = Stock
    template_name = 'inventory/stock_detail.html'

class StockCreateView(CreateView):
    model = Stock
    fields = ['product', 'quantity', 'location']
    template_name = 'inventory/stock_form.html'

class StockUpdateView(UpdateView):
    model = Stock
    fields = ['product', 'quantity', 'location']
    template_name = 'inventory/stock_form.html'

class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'inventory/stock_confirm_delete.html'
    success_url = '/stocks/'

# Order views
class OrderListView(ListView):
    model = Order
    template_name = 'inventory/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'inventory/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['product', 'quantity', 'order_source']
    template_name = 'inventory/order_form.html'

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['product', 'quantity', 'order_source']
    template_name = 'inventory/order_form.html'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'inventory/order_confirm_delete.html'
    success_url = '/orders/'

# Stock Transfer views
class StockTransferListView(ListView):
    model = StockTransfer
    template_name = 'inventory/stocktransfer_list.html'

class StockTransferDetailView(DetailView):
    model = StockTransfer
    template_name = 'inventory/stocktransfer_detail.html'

class StockTransferCreateView(CreateView):
    model = StockTransfer
    fields = ['product', 'from_location', 'to_location', 'quantity']
    template_name = 'inventory/stocktransfer_form.html'

class StockTransferUpdateView(UpdateView):
    model = StockTransfer
    fields = ['product', 'from_location', 'to_location', 'quantity']
    template_name = 'inventory/stocktransfer_form.html'

class StockTransferDeleteView(DeleteView):
    model = StockTransfer
    template_name = 'inventory/stocktransfer_confirm_delete.html'
    success_url = '/stocktransfers/'
