from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.
# 装饰器，非登录状态不可查看页面，会重定向至登录页面
@login_required
def index(request):
	"""主页视图"""
	posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'blogs/index.html', context)

def check_post_owner(request, post):
	"""检查帖子与当前用户是否关联"""
	if post.owner != request.user:
		raise Http404

@login_required
def new_post(request):
	"""新增帖子的视图"""
	if request.method != 'POST':
		# 未提交数据时，创建一个空白表单
		form = BlogPostForm()
	else:
		# 提及数据时，处理数据
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			# 将新帖子与当前用户关联
			new_post.owner = request.user
			new_post.save()
			return redirect('blogs:index')
	
	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

# 装饰器，非登录状态不可查看页面，会重定向至登录页面
@login_required
def edit_post(request, post_id):
	"""编辑帖子的视图"""
	post = get_object_or_404(BlogPost, id=post_id)
	# 检查帖子是否属于当前用户
	check_post_owner(request, post)
	if request.method != 'POST':
		form = BlogPostForm(instance=post)

	else:
		form = BlogPostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:index')

	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)


