from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Menu, name='menu'),
    path('/<int:cat>', views.Category_view, name='category_view'),
    path('/datail/<int:pk>', views.Datail.as_view(), name='datail'),
    path('/signup',views.Sign,name='sign'),
    path('/login', views.Login_View, name='login_view'),
    path('/logout', views.Loogout,name='logout'),
    path('/about', views.About, name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
