from django.contrib import admin
from .models import News, Course, Gallery, Admission, ContactInformation, Lecturer

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'is_published', 'created_at')
    list_filter = ('category', 'is_published', 'published_at')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    ordering = ('-published_at',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree', 'duration', 'tech_tags', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'tech_tags')
    list_editable = ('is_active',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active', 'link')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'university', 'phone', 'email')
    search_fields = ('dept_name', 'university', 'address', 'email')

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('full_name_th', 'full_name_en', 'expertise', 'is_head', 'order', 'is_active')
    list_filter = ('is_head', 'is_active', 'title')
    search_fields = ('first_name', 'last_name', 'full_name_en', 'expertise')
    list_editable = ('is_head', 'order', 'is_active')

