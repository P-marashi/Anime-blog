from django.db import models
from django.utils import timezone
from django.urls import reverse
from extensions.utils import jalali_converter
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField


# managers
class ArtManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def monthly_publish(self):
        return self.filter(best_status='y')

    class Meta:
        verbose_name = 'کتگوری '
        verbose_name_plural = 'کتگوری ها'

    def __str__(self):
        return self.title


class IPAddress(models.Model):
    user_ip = models.GenericIPAddressField(verbose_name="user_ip")

    def __str__(self):
        return self.user_ip


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', "منتشر شده"),
    )
    BEST_STATUS_CHOICES = (
            ('n', 'نیست'),
            ('y', "هست"),
    )
    title = models.CharField(
            max_length=200,
            verbose_name='عنوان مقاله',
            null=True,
    )

    slug = models.SlugField(
            max_length=100, unique=True,
            verbose_name='ادرس مقاله',
            null=True,
    )

    description_img = models.TextField(
        blank=False,
        verbose_name='متن زیر عکس'
    )
    description = RichTextUploadingField(
        verbose_name='متن مقاله'
    )

    ve_thumbnail = models.ImageField(
        upload_to="images",
        verbose_name='جلوه مقاله ',
        null=True,
    )

    thumbnail = models.ImageField(
        upload_to="images",
        verbose_name='تصویر مقاله',
        null=True,
    )
    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name='زمان انتشار'
    )
    creat = models.DateTimeField(
        auto_now_add=True,
    )
    update = models.DateTimeField(
        auto_now=True,
    )

    best_status = models.CharField(
        max_length=1,
        choices=BEST_STATUS_CHOICES,
        null=True,
        verbose_name='انیمه برتر ماه'
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='وضعیت'
    )


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def thumb_get(self):
        return format_html(f"""<img width=50 src='{self.ve_thumbnail.url}'""")

    @property
    def absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    objects = ArtManager()
