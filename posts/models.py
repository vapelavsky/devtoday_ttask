from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes_counter = models.IntegerField(default=0, editable=False)
    author = models.CharField(max_length=255)

    class Meta:
        ordering = ["created_at", "post_title"]


class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
