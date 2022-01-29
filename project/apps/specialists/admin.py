from django.contrib import admin

from .models import Department, Person


class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'published', 'department']
    list_filter = ['department']

    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Person, PersonAdmin)