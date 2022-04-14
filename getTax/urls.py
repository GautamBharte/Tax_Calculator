from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('submitQuery',views.submitQuery,name='submitQuery')
    path('submitquerry',views.submitquerry,name='submitquerry')
]