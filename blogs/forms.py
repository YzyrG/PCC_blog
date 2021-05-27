from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	"""创建帖子表单"""
	class Meta:
		model = BlogPost
		fields = ['title', 'text']
		labels = {'title':'帖子标题', 'text':'帖子内容'}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}
