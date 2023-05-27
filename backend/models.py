from django.db import models

class RD(models.Model):
    member = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    remarks = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} ({self.created_at})"
    

class DB(models.Model):
    member = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    remarks = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} ({self.created_at})"
