from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT = (('tanks', 'Танки'),
           ('healers', 'Хилы'),
           ('damage_dealers', 'ДД'),
           ('dealers', 'Торговцы'),
           ('gildmasters', 'Гилдмастеры'),
           ('quest_givers', 'Квестгиверы'),
           ('blacksmiths', 'Кузнецы'),
           ('tanners', 'Кожевники'),
           ('potion_makers', 'Зельевары'),
           ('spell_masters', 'Мастера заклинаний'))
    image = models.ImageField(upload_to='media/', blank=True)
    text = models.TextField()
    category = models.CharField(max_length=15, choices=CAT, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name='Название')
    objects = models.Manager()


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)