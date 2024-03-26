from django.db import models

# Create your models here.
class TodoItem(models.Model):
  title = models.CharField(max_length=256, null=True, blank=True)
  completed = models.BooleanField(blank=True, default=False)
  url = models.CharField(max_length=256, null=True, blank=True)
  order = models.IntegerField(null=True, blank=True)

  def __str__(self):
    model_name = self.__class__.__name__
    fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
    return f"{model_name}({fields_str})"
