# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Person(models.Model):
    businessentityid = models.IntegerField(db_column='BusinessEntityID',primary_key=True)  # Field name made lowercase.
    persontype = models.CharField(db_column='PersonType', max_length=2)  # Field name made lowercase.
    namestyle = models.BooleanField(db_column='NameStyle')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=8, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailpromotion = models.IntegerField(db_column='EmailPromotion')  # Field name made lowercase.
    additionalcontactinfo = models.TextField(db_column='AdditionalContactInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    demographics = models.TextField(db_column='Demographics', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowguid = models.CharField(max_length=36)
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[AdventureWorks2017].[Person].[Person]'

    def __str__(self):
        """
        String repping the model
        """
        return self.firstname
