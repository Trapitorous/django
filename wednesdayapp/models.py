from django.db import models
class Task(models.Model):
    title = models.charfield(max_length=20)
    Description = models.textfield(max_length=20)
    Completed = models.booleanfield(max_length=20)
    createdat = models.DateTimeField
    def __str__(self):
        return self.title

