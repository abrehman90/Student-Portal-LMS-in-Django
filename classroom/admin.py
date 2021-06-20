from django.contrib import admin
from classroom.models import Course, Category, Batch_Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


class batchCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Batch_Category,batchCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)