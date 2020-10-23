from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at',]


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title', ]
