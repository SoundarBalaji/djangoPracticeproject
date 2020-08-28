from django.db import models

class Collection(models.Model):
    collection_name=models.CharField(max_length=200)
    description=models.CharField(max_length=900)
    collcover=models.CharField(max_length=5000)

    def __str__(self):
        return self.collection_name


class Piece(models.Model):
    collection=models.ForeignKey(Collection, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    type=models.CharField(max_length=300)
    artist=models.CharField(max_length=300)
    year=models.IntegerField()
    piececover=models.CharField(max_length=5000)

    def __str__(self):
        return self.title


# Create your models here.
