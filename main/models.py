from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser

class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'

class Post(models.Model):

    title = models.CharField('Title (not required)', max_length=100, blank=True, null=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='Author'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Description of post (not required)')
    posted_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-posted_date',)



