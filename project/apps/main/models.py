from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from apps.services.models import Service

STATUS_CHOICES = (
    ('draft', 'Черновик'),
    ('published', 'Опубликовано'),
)
class Page(models.Model):
    MENU_CHOICES = (
        ('default', "По умолчанию"),
        ('main', "Главное меню"),
        ('footer', "Футер"),
    )

    menu = models.CharField(choices=MENU_CHOICES, default='default', max_length=20, verbose_name="Меню")
    name = models.CharField(max_length=200, verbose_name="Заголовок для меню")
    title = models.CharField(max_length=200, verbose_name="Заголовок для страницы")
    slug = models.SlugField(max_length=200, unique_for_date='created_at', verbose_name="Ярлык")
    description = RichTextField(verbose_name="Описание")
    is_show = models.BooleanField(default=False, verbose_name="Показывать в меню")
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    edited_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name="Статус")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок")

    def get_absolute_url(self):
        return '/page/%s' % self.slug

    def __str__(self):
        return '%s-%s' % (self.id, self.title)
    class Meta(object):
        db_table = "page"
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ['order']


class FreeCall(models.Model):
    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "free_call"
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'

    full_name = models.CharField(max_length=50, verbose_name="ФИО")
    e_mail = models.EmailField(verbose_name="Почта")
    subject = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    message = RichTextField(verbose_name="Сообшения", blank=True)
    phone_number = models.CharField(max_length=50, blank=True, verbose_name="Номер телефона")
    status = models.BooleanField(verbose_name="Обработана?", default=False)


class Result(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        db_table = "result"
        verbose_name = "Result"
        verbose_name_plural = "Results"

    id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    namein = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    norm = models.CharField(max_length=50)


class Lab(models.Model):
    def __str__(self):
        return self.id
    class Meta:
        db_table = "lab"
        verbose_name = "Lab"
        verbose_name_plural = "Labs"

    STATUSES = (
        (1, "1"),
        (2, "2"),
        (3, "3")
    )

    GERDERS = (
        (1, "Мужской"),
        (2, "Женский"),
    )

    id = models.CharField(max_length=20, unique=True, primary_key=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    client_code = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=STATUSES, default=1)
    gender = models.IntegerField(choices=GERDERS)
    oder_number = models.IntegerField(blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    list = models.ManyToManyField( Result, related_name="list", blank=True )