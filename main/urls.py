from django.urls import path
from . import views
from .views import home
from .views import landingPage

urlpatterns = [
    path('', home), # Includes the app's URL patterns
    path('landing/', views.landingPage, name='landing_page'),
    path('features/', views.votesInformation, name='features_page')
]