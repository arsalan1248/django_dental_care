from django.contrib import admin
from .models import User, TestKit

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", 'email')
    search_fields = (
        "username",
        "email",
    )

class TestKitAdmin(admin.ModelAdmin):
    list_display = ("test_kit_id",)


admin.site.register(User, UserAdmin)
admin.site.register(TestKit, TestKitAdmin)