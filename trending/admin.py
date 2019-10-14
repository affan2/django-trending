from django.contrib import admin

from .models import DailyViewSummary, ViewLog


class DailyViewSummaryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


class ViewLogAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]


admin.site.register(DailyViewSummary, DailyViewSummaryAdmin)
admin.site.register(ViewLog, ViewLogAdmin)
