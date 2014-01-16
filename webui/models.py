# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    run_status = models.CharField(max_length=8, blank=True)
    job_id = models.IntegerField()
    job_type = models.CharField(max_length=15)
    job_name = models.CharField(max_length=25, blank=True)
    extra_parameters = models.CharField(max_length=30)
    priority = models.IntegerField(blank=True, null=True)
    job_scheduler = models.CharField(max_length=15)
    submitted_date = models.DateTimeField()
    start_date = models.DateTimeField()
    complete_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'task'

class Component(models.Model):
    component_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, related_name='components')
    component_type = models.CharField(max_length=30)
    run_status = models.CharField(max_length=8, blank=True)
    extra_parameters = models.CharField(max_length=30)
    qsub_file = models.CharField(max_length=100, blank=True)
    qsub_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField()
    complete_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'component'

class Mail(models.Model):
    mail_id = models.IntegerField(primary_key=True)
    task_id = models.ForeignKey(Task, related_name='emails')
    email = models.CharField(max_length=40)
    sent = models.IntegerField(blank=True, null=True)
    added_date = models.DateTimeField()
    sent_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'mail'


