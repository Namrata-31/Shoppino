from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='uploads/shops/', default='')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_shops():
        return Shop.objects.all()
