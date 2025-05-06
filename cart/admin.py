from django.contrib import admin
from django.contrib.sessions.models import Session
from django.utils.html import format_html
import pprint

# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'safe_decoded_data', 'expire_date']

    def safe_decoded_data(self, obj):
        try:
            data = obj.get_decoded()
            formatted = pprint.pformat(data, indent=2)
            return format_html("<pre>{}</pre>", formatted)
        except Exception as e:
            return format_html("<pre>Error decoding: {}</pre>", str(e))

    safe_decoded_data.short_description = "Session Data"