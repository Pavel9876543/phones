from django.db import models
from django.urls import reverse


class Phones(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок')
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to="photos/")
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name="телефон"
        verbose_name_plural = "Телефоны"
        ordering = ['-time_create', 'title']



class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name="категорию"
        verbose_name_plural = "Категории"


class security(models.Model):
    login=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.login