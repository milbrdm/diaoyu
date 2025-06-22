from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('access-control/', views.AccessControlView.as_view(), name='access_control'),
    path('data-center/', views.DataCenterView.as_view(), name='data_center'),
    path('logs/', views.LogsView.as_view(), name='logs'),
    path('accounts/', views.AccountListView.as_view(), name='account_list'),
    path('roles/', views.RoleListView.as_view(), name='role_list'),
    path('access-records/', views.AccessRecordView.as_view(), name='access_records'),
    path('frontend/', views.FrontendConfigView.as_view(), name='frontend_config'),
    path('activation/', views.ActivationView.as_view(), name='activation'),
    path('version/', views.VersionView.as_view(), name='version'),
    path('settings/', views.SystemSettingView.as_view(), name='system_settings'),
    path('faq/', views.FAQView.as_view(), name='faq'),
]
