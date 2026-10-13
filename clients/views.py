from django.shortcuts import render, get_object_or_404  
from .models import Client

# Create your views here.
def dashboard(request):
    clients = Client.objects.all()
    return render(
        request,
        "clients/dashboard.html",
        {
           "clients":clients 
        }
    )

# Create another view client workspace  
def client_workspace(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(
        request,
        "clients/workspace.html",
        {
            "client":client 
        }
    )
