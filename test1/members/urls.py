from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('liste_cooperative/', views.liste_cooperative, name='liste_cooperative'),
    path('liste_cooperative/details_coop/<int:id>', views.details_coop, name='details_coop')

    
]