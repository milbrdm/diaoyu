from django.contrib import admin
from . import models

@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'last_login')

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'codename')

@admin.register(models.WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')

@admin.register(models.APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'method', 'status_code', 'timestamp')

@admin.register(models.AccessRecord)
class AccessRecordAdmin(admin.ModelAdmin):
    list_display = ('domain', 'ip', 'timestamp', 'blacklisted')

@admin.register(models.DomainConfig)
class DomainConfigAdmin(admin.ModelAdmin):
    list_display = ('domain', 'cert_path', 'is_active')

@admin.register(models.License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('code', 'expires_at', 'download_count')

@admin.register(models.SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
