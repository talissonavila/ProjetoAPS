from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import AddCommentForm, PostForm
from .models import Category, Comment, Post


class HomeView(ListView):
    """View for displaying the home page.

    Attributes:
        model (Post): Model for posts.
        template_name (str): Template for home page.
        ordering (list): Ordering for posts.
    """

    model = Post
    template_name = "home.html"
    ordering = ["-id"]

    def get_context_data(self, *args, **kwargs) -> dict:
        """Gets context data for the home page.

        Args:
            *args: Variable arguments.
            **kwargs: Keyword arguments.

        Returns:
            dict: Context data.
        """
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class ArticleDetailView(DetailView):
    """View for displaying article details.

    Attributes:
        model (Post): Model for posts.
        template_name (str): Template for article details.
    """

    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs) -> dict:
        """Gets context data for article details.

        Args:
            *args: Variable arguments.
            **kwargs: Keyword arguments.

        Returns:
            dict: Context data.
        """
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
    """View for adding a new post.

    Attributes:
        model (Post): Model for posts.
        form_class (PostForm): Form for adding a new post.
        template_name (str): Template for adding a new post.
    """

    model = Post
    form_class = PostForm
    template_name = "add_post.html"


class AddCategoryView(CreateView):
    """View for adding a new category.

    Attributes:
        model (Category): Model for categories.
        template_name (str): Template for adding a new category.
        fields (list): Fields for adding a new category.
    """

    model = Category
    template_name = "add_category.html"
    fields = "__all__"


class UpdatePostView(UpdateView):
    """View for updating a post.

    Attributes:
        model (Post): Model for posts.
        form_class (PostForm): Form for updating a post.
        template_name (str): Template for updating a post.

    Returns:
        None
    """

    model = Post
    form_class = PostForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    """View for deleting a post.

    Attributes:
        model (Post): Model for posts.
        template_name (str): Template for deleting a post.
        success_url (str): URL to redirect after deletion.
    """

    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class AddCommentView(CreateView):
    """View for adding a new comment.

    Attributes:
        model (Comment): Model for comments.
        form_class (AddCommentForm): Form for adding a new comment.
        template_name (str): Template for adding a new comment.
        success_url (str): URL to redirect after adding a comment.
    """

    model = Comment
    form_class = AddCommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form) -> object:
        """Validates the form for adding a new comment.

        Args:
            form (AddCommentForm): Form for adding a new comment.

        Returns:
            object: Validated form.
        """
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)


def CategoryView(request, slug) -> object:
    """View for displaying category posts.

    Args:
        request (object): Request object.
        slug (str): Category slug.

    Returns:
        object: Rendered template.
    """
    category_posts = Post.objects.filter(category=slug.replace("-", " "))
    return render(
        request, "categories.html", {"slug": slug.title().replace("-", " "), "category_posts": category_posts}
    )


def CategoryListView(request) -> object:
    """View for displaying category list.

    Args:
        request (object): Request object.

    Returns:
        object: Rendered template.
    """
    category_menu_list = Category.objects.all()
    return render(request, "category_list.html", {"category_menu_list": category_menu_list})


def LikeView(request, pk) -> object:
    """View for liking a post.

    Args:
        request (object): Request object.
        pk (int): Post ID.

    Returns:
        object: Redirect to article detail page.
    """
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))
