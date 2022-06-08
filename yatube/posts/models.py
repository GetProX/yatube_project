from django.db import models
from django.contrib.auth import get_user_model
#from django.utils.text import slugify



User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()


    def __str__(self):
        return self.title

#    def save(self, *args, **kwargs):
#       self.slug = slugify(self.title)
#        super(Group, self).save(*args, **kwargs)


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts'
    )


