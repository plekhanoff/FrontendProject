from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class GroupChat(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    messages = models.ManyToManyField(Message)

