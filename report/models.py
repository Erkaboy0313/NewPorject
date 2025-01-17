from django.db import models

class Report(models.Model):
    
    class StatusEnum(models.TextChoices):
        NEW = 'new'
        SEEN = 'seen'
    
    user = models.ForeignKey('user.Profile',on_delete=models.SET_NULL,null=True)
    blog = models.ForeignKey("blogging.Blog",on_delete=models.CASCADE)
    status = models.CharField(max_length=5,choices=StatusEnum.choices,default=StatusEnum.NEW)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)