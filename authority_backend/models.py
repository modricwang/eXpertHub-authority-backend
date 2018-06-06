from django.db import models


class shoppingcart(models.Model):
    uid = models.CharField(max_length=50)
    rid = models.CharField(max_length=50)


class access(models.Model):
    uid = models.CharField(max_length=50)
    rid = models.CharField(max_length=50)


class storage(models.Model):
    file = models.FileField()
    fid = models.IntegerField()
