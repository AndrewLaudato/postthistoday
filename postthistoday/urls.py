"""
URL Configuration for Post This Today
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Public pages
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about_page'),
    path('pricing/', views.pricing_page, name='pricing_page'),

    # Authentication (allauth)
    path('accounts/', include('allauth.urls')),

    # Protected app routes - redirect /app/ to mystyle
    path('app/', login_required(views.mystyle), name='app_home'),

    # Existing workflow routes (now protected with login_required)
    path('mystyle/', login_required(views.mystyle), name='mystyle'),
    path('trending_topics/', login_required(views.trending_topics), name='trending_topics'),
    path('content_prompt/', login_required(views.content_prompt), name='content_prompt'),
    path('customize_content/', login_required(views.customize_content), name='customize_content'),
    path('preview_and_share/', login_required(views.preview_and_share), name='preview_and_share'),
]