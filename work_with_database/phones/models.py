from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.ImageField(max_length=200)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, editable=False, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
