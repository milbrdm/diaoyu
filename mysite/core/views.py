from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from . import models

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

@method_decorator(login_required, name='dispatch')
class AccessControlView(TemplateView):
    template_name = 'core/access_control.html'

@method_decorator(login_required, name='dispatch')
class DataCenterView(ListView):
    model = models.WorkOrder
    template_name = 'core/data_center.html'
    context_object_name = 'workorders'

@method_decorator(login_required, name='dispatch')
class LogsView(ListView):
    model = models.APILog
    template_name = 'core/logs.html'
    context_object_name = 'logs'

@method_decorator(login_required, name='dispatch')
class AccountListView(ListView):
    model = models.Account
    template_name = 'core/account_list.html'
    context_object_name = 'accounts'

@method_decorator(login_required, name='dispatch')
class RoleListView(ListView):
    model = models.Role
    template_name = 'core/role_list.html'
    context_object_name = 'roles'

@method_decorator(login_required, name='dispatch')
class AccessRecordView(ListView):
    model = models.AccessRecord
    template_name = 'core/access_record.html'
    context_object_name = 'records'

@method_decorator(login_required, name='dispatch')
class FrontendConfigView(ListView):
    model = models.DomainConfig
    template_name = 'core/frontend_config.html'
    context_object_name = 'domains'

@method_decorator(login_required, name='dispatch')
class ActivationView(ListView):
    model = models.License
    template_name = 'core/activation.html'
    context_object_name = 'licenses'

@method_decorator(login_required, name='dispatch')
class VersionView(ListView):
    model = models.VersionLog
    template_name = 'core/version.html'
    context_object_name = 'versions'

@method_decorator(login_required, name='dispatch')
class SystemSettingView(ListView):
    model = models.SystemSetting
    template_name = 'core/system_settings.html'
    context_object_name = 'settings'

@method_decorator(login_required, name='dispatch')
class FAQView(ListView):
    model = models.FAQ
    template_name = 'core/faq.html'
    context_object_name = 'faqs'
