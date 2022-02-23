from Tasks import views 
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

app_name='Tasks'
urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('taskslist/',views.taskslist,name='taskslist'),
    path('displayall/',views.displayall,name='displayall'),
    path('delete/<str:name>',views.delete,name='delete'),
    path('update/<str:name>',views.update,name='update'),
    path('deleteall/',views.deleteall,name='deleteall'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('passwordreset/',views.passwordreset,name='passwordreset'),
    path('showimage',views.showimage,name='showimage'),
    path('deleteallimages/',views.deleteallimages,name='deleteallimages')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


