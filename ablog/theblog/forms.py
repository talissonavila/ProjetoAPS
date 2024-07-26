from django import forms

from .models import Post, Category,  Comment


class CategoryChoices:
    def __init__(self) -> None:
         self.choice_list = []
    
    def append_choices_item(self, item):
        self.choice_list.append(item)
    
    def get_choices(self):
        choices = Category.objects.all().values_list('name', 'name')
        for item in choices:
            self.append_choices_item(item)
        return self.choice_list

class PostForm(forms.ModelForm):
    class Meta:
        category_choices = CategoryChoices()
        model = Post
        fields = ('title', 'title_tag', "author", 'category', 'body', 'snippet', 'header_image')

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your post title here"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your post tag here (used in post title page)"}),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "user_id", "type": "hidden"}),
            "category": forms.Select(choices=category_choices.get_choices(), attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter your post content here"}),
            "snippet": forms.Textarea(attrs={"class": "form-control", "placeholder": "Describe your post abstract in 255 chars"}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        #TODO: Usar automaticamente o username em vez de deixar o usuario criar um nome
        model = Comment
        #fields =('body', )
        fields =('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            'body': forms.Textarea(attrs={"class": "form-control", "placeholder": "Add your comment here"}),
        }
