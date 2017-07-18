from django.contrib import admin
from .models import Apply

def apply_admin(modeladmin, request, queryset):
    queryset.update(status='u')


class ApplyAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'status']
    ordering = ['status']
    actions = [apply_admin]


# Register your models here.
admin.site.register(Apply, ApplyAdmin)