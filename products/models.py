from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name="Boshi", help_text="Bota boshi boladi", default="BOshi keladi")
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="media/products")
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    field1 = models.FileField(upload_to="media/products", default='asd')
    emailfield = models.EmailField(null=True, blank=True)
    field3 = models.BigIntegerField(blank=True, null=True)
    field4 = models.JSONField(blank=True, null=True)
    ip_field = models.GenericIPAddressField(blank=True, null=True)

    datefield = models.DateField(blank=True, null=True)
    datetimefield = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title