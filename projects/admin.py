from django.contrib import admin

from .models import Project, ProjectImage, TechTag


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_featured")
    list_filter = ("is_featured", "created_at")
    search_fields = ("title", "short_description", "long_description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tech_stack",)
    inlines = [ProjectImageInline]


@admin.register(TechTag)
class TechTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


