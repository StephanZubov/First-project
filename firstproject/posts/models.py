from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.text[0:100]
