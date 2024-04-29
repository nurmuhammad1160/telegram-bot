from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"
    



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    lesson_name = models.CharField(verbose_name="Dars nomi", max_length=255)
    lesson_number = models.IntegerField()
    videoId = models.CharField(verbose_name="videoni id raqami", max_length=200, null=True)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=False)
    telegram = models.CharField(verbose_name="Telegram man'ba", max_length=255, null=False)
    youtube = models.CharField(verbose_name="Youtube man'ba", max_length=255, null=False)

    # category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=20) 
    category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)
    # subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)

    def __str__(self):
        return f"№{self.id} - {self.lesson_name}"

# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     buyer = models.ForeignKey(User)
#     item_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20, verbose_name="Telefon")
