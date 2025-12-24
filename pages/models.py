from django.db import models


class SiteHero(models.Model):
    """Editable hero section content for the home page."""

    headline = models.CharField(max_length=120)
    subheadline = models.CharField(max_length=240, blank=True)
    intro_rich_text = models.TextField(help_text="You can use basic HTML for formatting.")

    class Meta:
        verbose_name = "Site hero"
        verbose_name_plural = "Site hero"

    def __str__(self) -> str:
        return self.headline


class AboutSection(models.Model):
    """Section-based layout for the About page."""

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    rich_text = models.TextField(help_text="You can use basic HTML for formatting.")

    class Meta:
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title


class AboutSectionImage(models.Model):
    """Optional images for each About section (inline in admin)."""

    section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="about/")
    alt_text = models.CharField(max_length=160, blank=True)

    def __str__(self) -> str:
        return self.alt_text or f"Image for {self.section.title}"


