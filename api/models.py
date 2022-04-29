from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField('Автор', max_length=50)
    comment = models.TextField('Комментарий')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.author

   