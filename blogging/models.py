from django.db import models


class Blog(models.Model):
    
    class StatusEnum(models.TextChoices):
        PUBLISHED = 'published'
        DRAFT = 'draft'
        BLOCKED = 'blocked'
    
    author = models.ForeignKey('user.Profile',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog_images/")
    likes = models.ManyToManyField("user.Profile",related_name='like_set')
    dislike = models.ManyToManyField("user.Profile",related_name='dislike_set')
    view = models.IntegerField(default=0)
    status = models.CharField(max_length=10,choices=StatusEnum.choices,default=StatusEnum.DRAFT)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    description = models.TextField()

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey("user.Profile",on_delete=models.CASCADE)
    text = models.TextField()
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    like = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    

    
    