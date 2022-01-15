from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('delivery', views.delivery, name = 'delivery'),
    path('faq', views.faq, name = 'faq'),
    path('info', views.info, name = 'info'),
    path('lk', views.lk, name = 'lk'),
    path('menu', views.menu, name = 'menu'),
    path('standart',views.standart_menu,name='standart_menu'),
    path('vegan',views.vegan_menu,name='vegan_menu'),
    path('order_step1', views.order_step1, name = 'step1'),
    path('order_step2', views.order_step2, name = 'step2'),
    path('order_step3', views.order_step3, name = 'step3'),
    path('order_step4', views.order_step4, name = 'step4'),

]