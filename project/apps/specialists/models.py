from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField



class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(verbose_name="Ярлык", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "departments"
        verbose_name = "Отделение"
        verbose_name_plural = "Отделение"


class Person(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    name = models.CharField(max_length=200, verbose_name="ФИО")
    image = ImageField(upload_to='images', blank=True, verbose_name="Изображение")
    description = RichTextField(verbose_name="Описание")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.SlugField(verbose_name="Ярлык", unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Рубрика', related_name='person_department')
    seo_title = models.CharField(max_length=200, verbose_name="SEO Title", blank=True)
    seo_description = models.CharField(max_length=300, verbose_name="SEO Description", blank=True)

    def get_absolute_url(self):
        return '%s-%s' % (self.slug, self.pk)
