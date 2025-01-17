from django.db import models

class Columns(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    descricao = models.TextField()
    columns = models.ForeignKey(Columns, on_delete=models.CASCADE)

    def __str__(self):
        return self.title