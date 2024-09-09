# catalogs/models.py

from django.db import models
from core.models import BaseModel

class CatalogBase(BaseModel):
    '''
    Базовая абстрактная модель для всех справочников системы, унаследованная от базового класса BaseModel 
    Является родителем для всех справочников.
    Атрибуты:
        унаследованные от BaseModel:
            created_at - дата и время создания элемента справочника (тип: DateTimeField)
            updated_at - дата и время обновления элемента справочника (тип: DateTimeField)
        дополнительные:
            name - имя элемента справочника, (по умолчанию для отображаемое элемента справочника пользователю) (тип: CharField)
    '''
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True
