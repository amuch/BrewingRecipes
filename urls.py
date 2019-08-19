from django.urls import path, include
from . import views

app_name = 'brew'

urlpatterns = [
    #path('', views.recipes, name = 'recipes'),
    path('hops/', views.hops, name = 'hops'),
    path('hops/<slug:hop>/', views.hop, name = 'hop'),

    path('malts/', views.malts, name = 'malts'),
    path('malts/<slug:malt>/', views.malt, name = 'malt'),

    path('styles/', views.styles, name = 'styles'),
    path('styles/<slug:style>/', views.style, name = 'style'),
]