from django.db import models


class Setting(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=50)
    short_desc = models.CharField(verbose_name="توضیحات کوتاه", max_length=120)
    about = models.TextField(verbose_name="درباره")
    email = models.EmailField(verbose_name="ایمیل پشتیبانی")
    phone = models.CharField(verbose_name="تلفن تماس", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'
