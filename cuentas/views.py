from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class LoginView(View):
	def get(self, request):
		template_name = "cuentas/login.html"
		return render(request, template_name)

class homeView(View):
	def get(self, request):
		home_name = "cuentas/home.html"
		return render(request, home_name)


