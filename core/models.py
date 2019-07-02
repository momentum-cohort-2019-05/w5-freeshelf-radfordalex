from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return 'Book: {}'.format(self.title)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    url = models.URLField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return 'Category: {}'.format(self.title)
    url = models.URLField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50)

# class Favorite(models.Model):
#     unique_together = [['book', 'user']]
#     def __str__(self):
#     return 'Favorite: {}'.format(self.title)
# ("Class Favorite" commented out because it currently breaks site.)