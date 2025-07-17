from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    readonly_fields = ('created_at',)

    def has_change_permission(self, request, obj=None):
        if not request.user.is_staff:
            return False
        if obj and obj.author != request.user and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff