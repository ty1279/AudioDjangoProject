from django.db import models
# Create your models here.

class Csv(models.Model):
    file_name = models.FileField(upload_to = 'myapp')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"


class Attribute(models.Model):
    age = models.IntegerField()
    accent_group = models.IntegerField()
    sex_in_number = models.IntegerField()

    def __str__(self):
        return f"{self.age}-{self.accent_group}"