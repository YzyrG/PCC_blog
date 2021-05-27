from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns =[
	# 主页页面
	path('', views.index, name='index'),
	# 新建帖子的页面
	path('new_post/', views.new_post, name='new_post'),
	# 编辑帖子的页面
	path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),

	]