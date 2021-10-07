from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core import views as core_views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('django.contrib.auth.urls')),
    path('profile/', include('user.urls')),
    
    path('',core_views.index),

    path('new/',core_views.newrepo,name='newrepo'),
    path('<user_profile>/<repo_name>/', core_views.viewrepo,name='viewrepo'),
    path('<user_profile>/<repo_name>/upload', core_views.uploadrepo,name='uploadrepo'),

    
]

urlpatterns += staticfiles_urlpatterns()