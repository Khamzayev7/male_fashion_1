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


class ProductModel(BaseModel):
    title = models.CharField(max_length=60, verbose_name=_("title"))
    short_description = models.CharField(max_length=255, verbose_name=_("short description"))
    long_description = RichTextUploadingField(verbose_name=_("long description"))
    price = models.FloatField(verbose_name=_("price"))
    real_price = models.FloatField(verbose_name=_("real price"), default=0)
    sale = models.BooleanField(verbose_name=_("sale"), default=False)
    discount = models.PositiveSmallIntegerField(verbose_name=_("discount"), default=0)
    main_image = models.ImageField(upload_to="media/shop_product/%Y/%m/%d", verbose_name=_("main image"))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("category")
    )
    tags = models.ManyToManyField(
        ProductTag,
        related_name="products",
        verbose_name=_("tags"),
    )





    

