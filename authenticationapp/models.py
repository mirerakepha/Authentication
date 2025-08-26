from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        width, height = img.size
        min_dim = min(width, height)

        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2

        img = img.crop((left, top, right, bottom))

        img = img.resize((300, 300), Image.Resampling.LANCZOS)


        img.save(self.image.path, optimize=True, quality=85)

