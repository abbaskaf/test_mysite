from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse
from .models import Category, Product, Image
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUp


def Menu(request):
    model = Product.objects.all()
    return render(request, 'menu.html', {'model': model})


# class Category_view(TemplateView):
#     template_name = 'categ.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cat = kwargs['cat']
#         post = get_object_or_404(Category,id=cat)
#         posty = Product.objects.filter(category_id=post)
#         context['post'] = post
#         context['posty'] = posty
#         return context
def Category_view(request, cat):
    try:
        post = Category.objects.get(id=cat)
        posty = Product.objects.filter(category_id=post)
        return render(request, 'categ.html', {'posty': posty})
    except:
        messages.success(request, 'دسته بندی صحیح را انتخاب کنید')
        return redirect('menu')


class Datail(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'datail.html'


def Sign(request):
    if request.method == "GET":
        form = SignUp
        return render(request, 'sign.html', {'form': form})
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت نام شما باموفقیت انجام شد')
            return redirect('menu')
        else:
            messages.error(request, 'لطفا فرم را بدرستی پر کنید')
            return redirect('sign')


def Login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'باموفقیت وارد شدید')
            return redirect('menu')
        else:
            messages.error(request, 'لطفا دوباره امتحان کنید')
            return redirect('login_view')
    else:
        return render(request, 'Login.html')


def Loogout(request):
    logout(request)
    messages.success(request,'باموفقیت خارج شدید')
    return redirect('menu')


def About(request):
    return render(request, 'about.html')
