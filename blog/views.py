from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.select_related().all()
    return render(
        request,
        "blog/blog_list.html",
        {
            "posts": posts,
        },
    )


def blog_detail(request, slug: str):
    post = get_object_or_404(
        BlogPost.objects.prefetch_related("images"),
        slug=slug,
    )
    return render(
        request,
        "blog/blog_detail.html",
        {
            "post": post,
        },
    )


