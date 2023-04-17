from django.contrib import admin

from webapp.models import Category, Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published']
    list_filter = ['title', 'experience_from', 'experience_to', 'category', 'is_published']
    search_fields = ['title']
    fields = ['title', 'salary', 'description', 'experience_from', 'experience_to', 'category', 'is_published',
              'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Category)
admin.site.register(Vacancy, VacancyAdmin)
