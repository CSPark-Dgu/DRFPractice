from django.conf import settings
from django.db import models


class Post(models.Model):  # versus DRF
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)
    photo = models.ImageField(blank=True, upload_to="instagram/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
