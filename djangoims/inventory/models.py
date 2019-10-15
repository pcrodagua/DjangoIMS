from django.db import models


class Device(models.Model):
    choices = (
        ('AVAIBLE', 'Ready to be purchased'),
        ('SOLD', 'Item sold'),
        ('RESTOCKING', 'Item restockin in few days')
    )
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    status = models.CharField(max_length=10, default="SOLD", choices=choices)
    issues = models.CharField(max_length=100, default="No issues")

    def __str__():
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

    class Meta:
        abstract = True


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
