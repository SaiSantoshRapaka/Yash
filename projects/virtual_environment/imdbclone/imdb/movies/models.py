from django.db import models

# Create your models here.
class generes(models.Model):
    genere = models.CharField(max_length=20, null = False, blank = False)

    def __str__(self):
        return self.genere


class movies(models.Model):
    movie_name = models.CharField(max_length=20, null=False, blank=False)
    hero = models.CharField(max_length=20, null=False, blank=False)
    heroine = models.CharField(max_length=20, null=False, blank=False)
    director = models.CharField(max_length=20, null=False, blank=False)
    release_date = models.DateField()
    genere = models.ForeignKey(generes,on_delete=models.DO_NOTHING)
    plot = models.TextField(max_length=200, null = True, blank= True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.movie_name