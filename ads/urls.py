from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


app_name = "ads"
schema_view = get_schema_view(
    openapi.Info(
        title="Barter Platform API",
        default_version='v1',
        description="Документация API для платформы обмена вещами",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", views.ad_list, name="ad_list"),
    path("ads/<int:pk>/", views.ad_detail, name="ad_detail"),
    path("ads/create/", views.ad_create, name="ad_create"),
    path("ads/<int:pk>/edit/", views.ad_edit, name="ad_edit"),
    path("ads/<int:pk>/delete/", views.ad_delete, name="ad_delete"),
    path("proposals/", views.proposal_list, name="proposal_list"),
    path("proposals/create/", views.proposal_create, name="proposal_create"),
    path('login/', auth_views.LoginView.as_view(template_name='ads/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ads:ad_list'), name='logout'),
    path('register/', views.register, name='register'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

