from django.contrib import admin

# Register your models here.
from habibas_blog.core.models import Post, Comment, PostLike, BlogOwner, ImageGallery


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogOwner)
class BlogOwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    pass