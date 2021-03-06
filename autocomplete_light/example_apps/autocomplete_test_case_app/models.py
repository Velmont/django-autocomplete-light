from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    groups = models.ManyToManyField('Group')


class Group(models.Model):
    name = models.CharField(max_length=100)


class NonIntegerPk(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    relation = models.ForeignKey('self', null=True, blank=True)
    noise = models.ForeignKey('basic.FkModel', null=True, blank=True)

    for_inline = models.ForeignKey('self', null=True, blank=True,
                                   related_name='inline')


class SubGroup(Group):
    pass


class CustomSchema(models.Model):
    name = models.CharField(primary_key=True, max_length=10, db_column='bar')

    class Meta:
        db_table = 'foobar'
