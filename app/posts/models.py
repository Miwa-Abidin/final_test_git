from django.db import models
from accounts.models import Author


class Post(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_rating(self):
        status_post = StatusPost.objects.filter(post=self).values('rating').last()
        return status_post


class Comment(models.Model):
    comment_text = models.TextField()
    comment_created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.post


class StatusPost(models.Model):
    RATING_CHOICE = (
        (0, 'nothing'),
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICE, null=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.post} - {self.rating} '