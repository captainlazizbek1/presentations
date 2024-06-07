from django.contrib import admin
from ads.models import Ads, Category

# Register your models here.

admin.site.register(Category)

# class AdsImageInline(admin.TabularInline):
#     model = AdsImage
#     extra = 5

class AdsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["name", ]}
    search_fields = ['title', 'description']
    list_filter = ['category','publish_time']


admin.site.register(Ads, AdsAdmin)
