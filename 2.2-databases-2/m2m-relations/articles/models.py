from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    items = models.ManyToManyField(Article, through='Relationship', related_name = 'scopes')

    class Meta:
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Relationship(models.Model):
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name = 'Раздел', related_name = 'relations')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name = 'Статья', related_name = 'relations')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
