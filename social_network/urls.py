
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


from account.views import RegisterView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/',RegisterView.as_view(),name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path ('api/',include('posts.urls')),
    path('api/friendship/',include('friendship.urls'))
    

]

if settings.DEVEL:
    urlpatterns += static('/media',document_root = settings.MEDIA_ROOT )
