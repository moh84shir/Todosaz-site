from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Todo(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=48)
    simple_desc = models.CharField(verbose_name="توضیحات کوتاه", max_length=80)
    created = models.DateTimeField(verbose_name="زمان ایجاد", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)
    text = models.TextField(verbose_name="متن")
    user = models.ForeignKey(User, verbose_name="کاربر", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "تودو"
        verbose_name_plural = "تودو ها"

    def get_absolute_url(self):
        return reverse("todoes:todo_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
