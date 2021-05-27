from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	"""帖子模型"""
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	# owner字段，建立到模型User的外键关联，用于将数据与特定用户关联
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""返回帖子标题"""
		return self.title