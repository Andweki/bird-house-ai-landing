from django.db import models

# Create your models here.
class Client (models.Model):
    name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    #Create a function to help use business name as a string
    def __str__(self):
        return self.business_name


#Create

class Conversation (models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="conversations")
    title = models.CharField(max_length=200,default="business research")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #create a function to help display title
    def __str__(self):
        return f"{self.title} - {self.client.business_name}"


class Message (models.Model):
    SENDER_CHOICES = [
        ("user","User"),
        ("ai","Ai assistant")
    ]
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name="messages")
    sender = models.CharField(max_length=10,choices=SENDER_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at","id"]

    def __str__(self):
        return f"{self.sender}: {self.content[:50]}"