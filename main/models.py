from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Sarlavha"))
    content = models.TextField(verbose_name=_("Maqola matni"))
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Maqola")
        verbose_name_plural = _("Maqolalar")

    def __str__(self):
        return self.title