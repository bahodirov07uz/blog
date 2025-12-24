from django.contrib import admin

from .models import AboutSection, AboutSectionImage, SiteHero


@admin.register(SiteHero)
class SiteHeroAdmin(admin.ModelAdmin):
    list_display = ("headline", "subheadline")


class AboutSectionImageInline(admin.TabularInline):
    model = AboutSectionImage
    extra = 1


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [AboutSectionImageInline]
    ordering = ("order",)


