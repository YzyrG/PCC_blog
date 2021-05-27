from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
	"""注册新用户"""
	if request.method != 'POST':
		# 未提交数据，显示空表单
		form = UserCreationForm()
	else:
		# 提交了数据，处理表单数据
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			# 表单数据有效，保存数据
			new_user = form.save()
			# 让用户自动登录，并重定向至主页
		login(request, new_user)
		return redirect('blogs:index')
		
		# 显示空表单或指出数据无效
	context = {'form': form}
	return render(request, 'registration/register.html', context)
