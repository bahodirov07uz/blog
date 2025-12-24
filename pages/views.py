from django.shortcuts import render

from blog.models import BlogPost
from .models import AboutSection, SiteHero


def home(request):
    hero = SiteHero.objects.first()
    latest_posts = BlogPost.objects.select_related().order_by("-created_at")[:3]
    return render(
        request,
        "pages/home.html",
        {
            "hero": hero,
            "latest_posts": latest_posts,
        },
    )


def about(request):
    sections = AboutSection.objects.prefetch_related("images").all()
    return render(
        request,
        "pages/about.html",
        {
            "sections": sections,
        },
    )


