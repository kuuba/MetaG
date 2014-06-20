from django.db import models
from django.contrib.auth.models import User
import hashlib

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    ## probably requires import from somewhere (Authentication)
    ##project_owner = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectFileTable(models.Model):
    project = models.ForeignKey(Project)
    fileid = models.IntegerField()

"""
class SequenceFile(models.Model):
    def file_hash(file_name):
        BLOCKSIZE = 65536
        hasher = hashlib.md5()
        with open(file_name, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
            afile.close()
        return hasher.digest()
    project = models.ForeignKey(Project)
    oligo_file = models.FilePathField()
    oligo_hash = models.BinaryField()
    sff_file = models.FilePathField()
    sff_hash = models.BinaryField()
    creation_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)


class SequenceRun(models.Model):
    input_sequence = models.ForeignKey(SequenceFile)
    sequencing_no = models.IntegerField()
    run_state = models.CharField(max_length=8)
    output_file = models.FilePathField()
"""
