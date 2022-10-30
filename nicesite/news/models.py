from django.db import models

class News(models.Model) :
    objects = None
    title = models.CharField(max_length=150 , verbose_name='Новость')
    content = models.TextField(blank=True , verbose_name='контент')
    photo = models.ImageField(upload_to='photos/%Y/%M/%d/' , verbose_name='Фото' , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , verbose_name= 'Дата публикации')
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True , verbose_name='Опубликовано')
    category = models.ForeignKey('Category' , on_delete=models.PROTECT , null=True , blank=True , verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

class Category(models.Model) :
    objects = None
    title = models.CharField(max_length=250 , db_index=True , verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'






