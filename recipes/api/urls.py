from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('styles/', views.StyleListView.as_view(), name = 'style_list'),
    path('styles/<pk>', views.StyleDetailView.as_view(), name = 'style_detail'),
    path('malts/', views.MaltListView.as_view(), name = 'malt_list'),
    path('malts/<pk>', views.MaltDetailView.as_view(), name = 'malt_detail'),
]
