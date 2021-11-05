from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return f'{self.id} | {self.title}, {self.description[:10]}'
