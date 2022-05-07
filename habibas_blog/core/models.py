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
    catchy_title = models.TextField()
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

    def likes_count(self):
        likes_count = list(PostLike.objects.filter(post_id=self.id))
        return len(likes_count)

    def comments_count(self):
        comments_count = list(Comment.objects.filter(post_id=self.pk))
        return len(comments_count)

class PostLike(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user_id = models.ForeignKey(to=UserModel, on_delete=models.CASCADE,)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

