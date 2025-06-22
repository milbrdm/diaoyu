from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Account(AbstractUser):
    roles = models.ManyToManyField(Role, blank=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('bound', 'Bound'),
        ('done', 'Done'),
        ('garbage', 'Garbage'),
        ('blacklist', 'Blacklist'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='workorders_created')
    assigned_to = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='workorders_assigned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class APILog(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.PositiveSmallIntegerField()
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

class AccessRecord(models.Model):
    domain = models.CharField(max_length=255)
    browser = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100)
    user = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)
    blacklisted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

class DomainConfig(models.Model):
    domain = models.CharField(max_length=255)
    cert_path = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain

class License(models.Model):
    code = models.CharField(max_length=100, unique=True)
    expires_at = models.DateTimeField()
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code

class VersionLog(models.Model):
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.version

class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField(blank=True)

    def __str__(self):
        return self.key

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question
