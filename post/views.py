from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect, render

from post.forms import PostCreateForm, PostModelForm
from post.models import Post


@login_required
def post_list(request):
    posts = Post.objects.filter(user=request.user)
    return render(
        request,
        "post/list.html",
        context={
            "posts": posts,
        },
    )


@login_required
def post_create(request):
    if request.method == "GET":
        form = PostCreateForm()
        return render(
            request,
            "post/create.html",
            context={"form": form},
        )
    else:
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print("form data sent through html form", form.cleaned_data, request.POST)
            post = Post.objects.create(
                title=form.cleaned_data.get("title"),
                content=form.cleaned_data.get("content"),
                image=form.cleaned_data.get("image"),
                user=request.user,
            )
            return redirect("post-list")
        return render(
            request,
            "post/create.html",
            context={"form": form},
        )


@login_required
def post_edit(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id, user=request.user)
        form = PostModelForm(instance=post)
        return render(
            request,
            "post/edit.html",
            context={
                "post": post,
                "form": form,
            },
        )
    else:
        post = Post.objects.get(id=id, user=request.user)
        form = PostModelForm(
            instance=post,
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            return redirect("post-list")
        return render(
            request,
            "post/edit.html",
            context={"post": post, "form": form},
        )


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(
        request,
        "post/detail.html",
        {
            "post": post,
        },
    )


@login_required
def post_delete(request, id):
    try:
        post = Post.objects.get(id=id, user=request.user)
        post.delete()
        return redirect("post-list")
    except Exception as e:
        return render(request, "errors/404.html", {"exception": e})
