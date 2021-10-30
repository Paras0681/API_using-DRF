from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    # This route can be used for using token authentication which get's the token when we go to this url
    # path('api-token-auth/', views.obtain_auth_token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token-refresh')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
