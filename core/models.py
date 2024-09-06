# core/models.py
from django.db import models

# Модель, которая может быть расширена объектами метаданных
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
