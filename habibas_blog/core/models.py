from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    image_url = models.URLField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user_id = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']