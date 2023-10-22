from django.db import models
from django.urls import reverse


class Zodiac_signs_prognoz(models.Model):
    title = models.CharField(max_length=255)
    date = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'zodiac': self.url})