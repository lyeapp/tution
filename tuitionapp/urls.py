from django.urls import path
from tuitionapp import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('loginpage',views.loginpage,name='loginpage'),
   
    path('about',views.about,name='about'),
   
    path('usercreate',views.usercreate,name='usercreate'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('addc',views.addc,name='addc'),
    path('addclass',views.addclass,name='addclass'),
    path('show_c',views.show_c,name='show_c'),
    path('edit_c/<int:pk>',views.edit_c,name='edit_c'),
    path('delete_c/<int:pk>',views.delete_c,name='delete_c'),
    path('addt',views.addt,name='addt'),
    path('addtutor',views.addtutor,name='addtutor'),
    path('show_t',views.show_t,name='show_t'),
    path('edit_t/<int:pk>',views.edit_t,name='edit_t'),
    path('/delete_t/<int:pk>',views.delete_t,name='delete_t'),
    path('adds',views.adds,name='adds'),
    path('addstud',views.addstud,name='addstud'),
    path('show_s',views.show_s,name='show_s'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_s/<int:pk>',views.edit_s,name='edit_s'),
    path('delete_s/<int:pk>',views.delete_s,name='delete_s'),
    path('profile',views.profile,name='profile'),
]
