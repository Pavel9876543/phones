from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('android', android, name='android'),
    path('iphone', iphone, name='iphone'),
    path('samsung', samsung, name='samsung'),
    path('cats/<slug:cat_slug>/', show_category, name='cats'),
    path('dg/', dg, name='dg'),
    path('nokia/', nokia, name='Nokia'),
    path('blackview/',  blackview, name='blackview'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('post/<int:post_id>/', show_post, name='post'),
    path('secr', secr, name='secr'),
    path('add_page', addpage, name='add_page'),
]