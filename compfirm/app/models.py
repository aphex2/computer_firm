from django.db import models
from django.utils.translation import ugettext as _


class Product(models.Model):
    maker = models.CharField(verbose_name=_("Maker"), max_length=10)
    model = models.CharField(verbose_name=_("Model"), max_length=50, primary_key=True)
    type = models.CharField(verbose_name=_("Type"), max_length=50)

    def __unicode__(self):
        return "%s - %s" % (self.model, self.maker)


class Laptop(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product)
    speed = models.SmallIntegerField(verbose_name=_("Speed"))
    ram = models.SmallIntegerField(verbose_name=_("RAM"))
    hd = models.FloatField(verbose_name=_("HDD"))
    price = models.DecimalField(verbose_name=_("Price"), max_digits=12, decimal_places=2, null=True)
    screen = models.SmallIntegerField(verbose_name=_("Screen size"))

    def __unicode__(self):
        return "%s" % self.model


class PC(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product)
    speed = models.SmallIntegerField(verbose_name=_("Speed"))
    ram = models.SmallIntegerField(verbose_name=_("RAM"))
    hd = models.FloatField(verbose_name=_("HDD"))
    cd = models.CharField(verbose_name=_("CD"), max_length=10)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=12, decimal_places=2, null=True)

    def __unicode__(self):
        return "%s" % self.model


class Printer(models.Model):
    code = models.AutoField(primary_key=True)
    model = models.ForeignKey(Product)
    color = models.CharField(verbose_name=_("Color"), max_length=2)
    type = models.CharField(verbose_name=_("Type"), max_length=10)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=12, decimal_places=2, null=True)

    def __unicode__(self):
        return "%s" % self.model
