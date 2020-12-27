from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('signup', views.signup, name="signup"),
    path('log', views.log, name="log"),
    path('home', views.home, name="home"),
    path('sign', views.sign, name="sign"),
    path('add/<slug:username>/<slug:eotp>/<slug:potp>/', views.add, name='add'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)