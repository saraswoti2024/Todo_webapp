from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:id>',edit,name="edit"),  # Fix edit path
    path('delete/<int:id>/', delete, name="delete"),  # Fix delete path
    path('complete/',complete,name="complete"),
     path('deletes/<int:id>/', deletes, name="deletes"),
]