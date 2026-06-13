from django.db import models
from django.utils.translation import gettext_lazy as _  # 1. Shu importni qo'shing

class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) # <--- SHUNI QO'SHING

    class Meta:
        verbose_name = _("Maqola")          # Birlik formasi uchun tarjima
        verbose_name_plural = _("Maqolalar") # Ko'plik formasi uchun tarjima