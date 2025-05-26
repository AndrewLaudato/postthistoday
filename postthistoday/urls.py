# Update your postthistoday/urls.py to include step 5:
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.writing_samples, name='writing_samples'),
    path('trending_topics/', views.trending_topics, name='trending_topics'),
    path('content_prompt/', views.content_prompt, name='content_prompt'),
    path('customize_content/', views.customize_content, name='customize_content'),
    path('preview_and_share/', views.preview_and_share, name='preview_and_share'),  # Add this line
]