from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('short_content', 'user_display', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('content', 'user__username')
    readonly_fields = ('content', 'user', 'created_at')

    def short_content(self, obj):
        return obj.content[:50] + ("..." if len(obj.content) > 50 else "")
    short_content.short_description = "Content"

    def user_display(self, obj):
        return obj.user.username if obj.user else "Anonymous"
    user_display.short_description = "User"

    def has_add_permission(self, request):
        return False  # ไม่ให้เพิ่มผ่าน Admin