from django.db import models


class Coffee(models.Model):
    title = models.CharField(max_length=200)
    coffee = models.CharField(max_length=100)
    syrup = models.CharField(max_length=100, null=True, blank=True)
    amount_of_milk = models.IntegerField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
