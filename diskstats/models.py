from django.db import models

class diskusage(models.Model):
    id = models.AutoField(primary_key=True)
    root_dir = models.CharField(max_length=50, blank=True)
    directory = models.CharField(max_length=50, blank=True)
    size = models.IntegerField()
    checkdate = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'diskusage'

# Create your models here.
