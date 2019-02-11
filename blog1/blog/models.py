from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)#设置字段
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)#允许通过类User反向查询到BlogArticle
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)#注意一下
    class Meta:
        ordering = ("-publish",)#规定BLogArticles实例对象按照publish倒叙显示
    def __str__(self):
        return self.title
# Create your models here.
