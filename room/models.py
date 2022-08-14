from django.db import models
from core.models import User
from core.models import Group


class Room(models.Model):
    name = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(unique=True)
    #edited this line (i added thsi to select multiple groups) - dinesh 
    enroll_aluminis = models.ManyToManyField(User)
    #upto this -dinesh
    
    def __str__(self):
        return self.name.group_name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name = 'message', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = 'message', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
