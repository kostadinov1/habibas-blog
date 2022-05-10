from django.contrib import admin

# Register your models here.
from habibas_blog.core.models import Post, Comment, PostLike, BlogOwner, ImageGallery, CommentLike, OwnerArticle


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'catchy_title', 'status', 'created_on')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'post','active', 'created_on')


@admin.register(CommentLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_on')



@admin.register(BlogOwner)
class BlogOwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(OwnerArticle)
class OwnerArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_image', 'created_on')
    list_filter = ('cover_image',)