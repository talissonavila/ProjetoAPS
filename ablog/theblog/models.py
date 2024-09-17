from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Category model.

    Attributes:
        name (str): Category name.
    """

    class Meta:
        """Category Metadata."""

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Returns the category name."""
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    """Post model.

    Attributes:
        title (str): Post title.
        title_tag (str): Post title tag.
        author (User): Post author.
        body (RichTextField): Post body.
        post_date (datetime): Post date.
        category (str): Post category.
        snippet (str): Post snippet.
        likes (ManyToManyField): Post likes.
        header_image (ImageField): Post header image.

    """

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default=author)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self) -> str:
        """Returns the post title and author."""
        return self.title + " | " + str(self.author)

    def total_likes(self) -> int:
        """Returns the total number of likes for the post."""
        return self.likes.count()

    def get_absolute_url(self) -> str:
        """Returns the absolute URL for the post."""
        return reverse("home")


class Profile(models.Model):
    """Profile model.

    Attributes:
        user (User): Profile user.
        bio (str): Profile bio.
        profile_picture (ImageField): Profile picture.
        website_url (str): Profile website URL.
        github_url (str): Profile GitHub URL.
        linkedin_url (str): Profile LinkedIn URL.
        instagram_url (str): Profile Instagram URL.
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, blank=True, null=True)
    github_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        """Returns the profile user."""
        return str(self.user)

    def get_absolute_url(self) -> str:
        """Returns the absolute URL for the profile."""
        return reverse("home")


class Comment(models.Model):
    """Comment model."""

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Returns the comment body."""
        return "%s - %s " % (self.post.title, self.name)
