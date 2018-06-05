from django.db import models


class shoppingcart(models.Model):
    uid = models.IntegerField()
    rid = models.IntegerField()


class access(models.Model):
    uid = models.IntegerField()
    rid = models.IntegerField()
