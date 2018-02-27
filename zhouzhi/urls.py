"""zhouzhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from zhou import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^question/(\d+)/$', views.answer, name='question_id'),
    url(r'^change',views.change_password),
    url(r'^answer',views.answer),
    url(r'^persion_integral', views.persion_integral),
    url(r'^persioncenter', views.persion_center),
    url(r'^persion', views.persion),
    url(r'^changepass', views.change_password),
    url(r'^accounts/login/',views.userlogin),
    url(r'^search_after', views.search),
    url(r'^search',views.before_search),
    url(r'^hot',views.hot),
    url(r'^bundling', views.send_bundling_qq),
    url(r'^rebundling', views.re_bundling_qq),
    url(r'^register',views.register),
    url(r'^login',views.userlogin),
    url(r'^logout',views.userlogout),
    url(r'^perion_anwser',views.perion_anwser),
]
