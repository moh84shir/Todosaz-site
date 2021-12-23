from django.db import models
from django.urls import reverse


class New(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=50)
    subject = models.CharField(verbose_name="موضوع", max_length=120)
    short_desc = models.CharField(verbose_name="توضیحات کوتاه", max_length=200)
    text = models.TextField(verbose_name="متن")
    pub_date = models.DateField(verbose_name="روز انتشار", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="فعال است/نیست", default=False)

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"

    def get_absolute_url(self):
        return reverse("news:new_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
