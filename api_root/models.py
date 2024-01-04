from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        """
        Method to show an customize phrase on admin screen to each item
        """
        return f'{self.name} - {self.description}'