from django.db import models

class ChangeLog(models.Model):
    type_of_change= models.CharField(max_length=50)
    change= models.TextField()
    change_time= models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("ChangeLog")
        verbose_name_plural = ("ChangeLogs")

    def __str__(self):
        return self.change
