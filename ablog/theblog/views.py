from re import A
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404

from .models import Category, Post, Comment
from .forms import PostForm, AddCommentForm

# self = request

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # order per post date from most recent day
    #ordering = ["-post_date"]
    # order per most recent id post
    ordering = ["-id"]

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
        

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        likes_in_post = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = likes_in_post.total_likes()
        liked = False

        if likes_in_post.likes.filter(id=self.request.user.id).exists():
           liked = True 

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # para usar todos os campos classe Post no form
    #fields = "__all__"
    # para personalizar o form do post baseado na classe Post
    #fields  = ("title", "title_tag", "body")


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "update_post.html"
    #fields = ["title", "title_tag", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)


def CategoryView(request, slug):
    category_posts = Post.objects.filter(category=slug.replace('-', ' '))
    return render(request, 'categories.html', {'slug': slug.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'category_menu_list': category_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))
