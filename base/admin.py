from django.contrib import admin

# Register your models here.
from .models import Room,Topic,Message,User #This imports the room model

admin.site.register(User)
admin.site.register(Room) #This registers the room model to the database
admin.site.register(Topic)
admin.site.register(Message)