from django.urls import path
from . import views

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("<int:client_id>/",views.client_workspace,name="client_workspace") 
]
