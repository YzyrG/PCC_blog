from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
	# 使用默认的身份验证url模式
	path('', include('django.contrib.auth.urls')),
	# 用户注册页面
	path('register/', views.register, name='register'),


	]