from django.db import models


class ownership(models.Model):
    uid = models.IntegerField
    rid = models.IntegerField


class access(models.Model):
    uid = models.IntegerField
    rid = models.IntegerField
