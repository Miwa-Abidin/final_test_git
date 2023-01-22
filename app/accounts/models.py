
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    telegram_chat_id = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return self.user.username