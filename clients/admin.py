from django.contrib import admin
from .models import Client,Conversation,Message 

# Register your models here.
admin.site.register(Client)
admin.site.register(Conversation)
admin.site.register(Message)
