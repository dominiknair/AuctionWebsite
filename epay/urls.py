from django.urls import path
from .views import ItemListView,ItemDetailView,ItemCreateView,ItemUpdateView,ItemDeleteView
from . import views

urlpatterns = [
    path('', ItemListView.as_view(), name='epay-Home'),
    path('signup/', views.signup, name='epay-signup'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('search/', views.searchView, name='searchview'),
    path('search1/', views.searchView1, name='searchview1'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('bid/', views.bidView, name='bidView'),
    path('countdownExpired/',views.turntoClosed,name='turntoClosed'),
    path('closedbids/',views.closedbids,name='closedbids'),
]
