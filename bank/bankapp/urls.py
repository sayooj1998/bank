
from django.urls import path

from bankapp import views
app_name='bankapp'
urlpatterns = [

    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('reg/', views.reg, name="reg"),
    path('new/',views.new,name="new"),
    path('regcheck',views.regcheck,name="regcheck"),
    path('logcheck',views.logchech,name="logcheck"),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX


]
