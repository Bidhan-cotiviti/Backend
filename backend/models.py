from django.db import models

class RD(models.Model):
    emp_id = models.IntegerField()
    member = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"( Member: {self.member}, Position: {self.position}, Remarks: {self.remarks}, Date: {self.created_at.date()})"
    

class DB(models.Model):
    emp_id = models.IntegerField()
    member = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"( Member: {self.member}, Position: {self.position}, Remarks: {self.remarks}, Date: {self.created_at.date()})"
    
