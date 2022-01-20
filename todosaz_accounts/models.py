from django.db import models
from django.contrib.auth.models import User


class ProfileImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="ProfileImages/%D")

    def get_image_url(self):
        return self.image.url



class AboutUser(models.Model):
    about = models.TextField(verbose_name="درباره ی شخص")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return self.user