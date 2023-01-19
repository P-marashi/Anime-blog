from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# managers
class ArtManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def cat_pub(self):
        return self.filter(status=True)


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name='عنوان کتگوری')
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='ادرس کتگوری')
    status = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')
    position = models.IntegerField(verbose_name='بوزیشن')

    class Meta:
        verbose_name = 'کتگوری '
        verbose_name_plural = 'کتگوری ها'

    def __str__(self):
        return self.title

class Pub(models.Model):
   title = models.CharField(max_length=200, null=True, verbose_name='عنوان کتگوری')

   def __str__(self):
       return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', "منتشر شده"),
    )
    title = models.CharField(max_length=200, null=True, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='ادرس مقاله')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name="articles")
    description = RichTextUploadingField(verbose_name='متن مقاله')
    description_img = models.TextField(default=True,verbose_name='متن زیر عکس')
    thumbnail = models.ImageField(upload_to="images", null=True, verbose_name='تصویر مقاله')
    ve_thumbnail = models.ImageField(upload_to="images", null=True, verbose_name='جلوه مقاله ')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    creat = models.DateTimeField(auto_now_add=True, )
    update = models.DateTimeField(auto_now=True, )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def cat_publish(self):
        return self.category.filter(status=True)

    def thumb_get(self):
        return format_html(f"""<img width=50 src='{self.ve_thumbnail.url}'""")



    objects = ArtManager()




