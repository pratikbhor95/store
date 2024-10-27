from django.contrib import admin
from home.models import Message , Items 

# Register your models here.
@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Items._meta.get_fields()]

# class ImageAdmin(admin.ModelAdmin):
#     list_display = "__all__"

admin.site.register(Message),
# admin.site.register(Image),