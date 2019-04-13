from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Mem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='mems', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('mem-detail', kwargs={'pk': self.pk})
