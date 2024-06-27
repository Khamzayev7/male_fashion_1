from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from shop.abstract import BaseModel

UserModel = get_user_model()

class Category(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class ProductTag(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        self.name

    class Meta:
        db_table = "Product tag"
        verbose_name = "Tag"
        verbose_name_plural = "tags"  

class BrendModel(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        self.name

    class Meta:
        db_table = "Product brand"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

class SizeModel(BaseModel):
    name = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        self.name

    class Meta:
        db_table = "Product size"
        verbose_name = "Size"
        verbose_name_plural = "Sizes"     

class ColorModel(BaseModel):
    code = models.CharField(max_length=60, verbose_name=_("name"))

    def __str__(self) -> str:
        self.code

    class Meta:
        db_table = "Product color"
        verbose_name = "Color"
        verbose_name_plural = "Colors"        





    

