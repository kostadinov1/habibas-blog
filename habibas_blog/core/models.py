from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from habibas_blog.common.validators import validate_only_letters, MaxFileSizeInMbImageValidator

UserModel = get_user_model()


class BlogOwner(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    IMAGE_MAX_SIZE = 5

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, blank=False, null=False,
                                  validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH), validate_only_letters))
    last_name = models.CharField(max_length=30, blank=False, null=False,
                                 validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH), validate_only_letters))
    url_image = models.URLField(blank=True, null=True)
    local_image = models.ImageField(blank=True, null=True, upload_to='owner_images',
                                    validators=(MaxFileSizeInMbImageValidator(IMAGE_MAX_SIZE),))

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class OwnerArticle(models.Model):
    TITLE_MAX_LEN = 50

    title = models.CharField(max_length=TITLE_MAX_LEN, null=False, blank=False)
    image = models.URLField(null=True, blank=True)
    cover_image = models.BooleanField(default=False)
    right = models.BooleanField(default=True)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class ImageGallery(models.Model):
    TITLE_MAX_LEN = 50
    IMAGE_MAX_SIZE = 5

    title = models.CharField(null=False, blank=False, max_length=TITLE_MAX_LEN)
    local_image = models.ImageField(blank=True, null=True, upload_to='images',
                                    validators=(MaxFileSizeInMbImageValidator(IMAGE_MAX_SIZE),))
    cover_image = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    TITLE_MAX_LEN = 200

    title = models.CharField(max_length=TITLE_MAX_LEN, unique=True, null=False, blank=False)
    catchy_title = models.TextField(null=False, blank=False)
    image_url = models.URLField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

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
    content = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def likes_count(self):
        likes_count = list(CommentLike.objects.filter(comment_id=self.id))
        return len(likes_count)


class CommentLike(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
