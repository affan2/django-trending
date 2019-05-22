from django.contrib import admin

from .models import DailyViewSummary, ViewLog


admin.site.register(DailyViewSummary)
admin.site.register(ViewLog)
