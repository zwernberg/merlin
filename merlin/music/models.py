from django.db import models
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title

class Song(SortableMixin):
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Songs'

    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    fan_votes = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, blank=True, null=True, related_name = 'songs')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.title
