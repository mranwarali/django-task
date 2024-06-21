from django.urls import path
from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    StockListView, StockDetailView, StockCreateView, StockUpdateView, StockDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    StockTransferListView, StockTransferDetailView, StockTransferCreateView, StockTransferUpdateView, StockTransferDeleteView
)

urlpatterns = [
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Stock URLs
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
    path('stocks/add/', StockCreateView.as_view(), name='stock-add'),
    path('stocks/<int:pk>/edit/', StockUpdateView.as_view(), name='stock-edit'),
    path('stocks/<int:pk>/delete/', StockDeleteView.as_view(), name='stock-delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/add/', OrderCreateView.as_view(), name='order-add'),
    path('orders/<int:pk>/edit/', OrderUpdateView.as_view(), name='order-edit'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

    # Stock Transfer URLs
    path('stocktransfers/', StockTransferListView.as_view(), name='stocktransfer-list'),
    path('stocktransfers/<int:pk>/', StockTransferDetailView.as_view(), name='stocktransfer-detail'),
    path('stocktransfers/add/', StockTransferCreateView.as_view(), name='stocktransfer-add'),
    path('stocktransfers/<int:pk>/edit/', StockTransferUpdateView.as_view(), name='stocktransfer-edit'),
    path('stocktransfers/<int:pk>/delete/', StockTransferDeleteView.as_view(), name='stocktransfer-delete'),
]
