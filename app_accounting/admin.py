from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_accounting.models import User, MessagingModel, ConsultingModel, NewsletterModel, BlogPostModel
from django.utils.translation import gettext_lazy as _


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {
            "fields": (
                #"id",
                ("first_name", "last_name"),
                "email",
                "avatar",
                "about",
            ),
        }),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class MessagingAdmin(admin.ModelAdmin):
    title = 'messaging_users'
    list_display = ("id", "email", "phone_number", "your_comment")
    def get_queryset_for_request_user(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class ConsultingAdmin(admin.ModelAdmin):
    title = 'consulting_users'
    list_display = ("email", "phone_number")
    def get_queryset_for_request_user(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class NewsletterAdmin(admin.ModelAdmin):
    title = 'newsletter_users'
    list_display = ("email",)
    def get_queryset_for_request_user(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "published_date")

    def get_queryset(self, request):
        current_user = request.user
        qs = super().get_queryset(request)
        return qs.filter(user=current_user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(MessagingModel, MessagingAdmin)  
admin.site.register(ConsultingModel, ConsultingAdmin) 
admin.site.register(NewsletterModel, NewsletterAdmin)
admin.site.register(BlogPostModel, BlogPostAdmin)  
