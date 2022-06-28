from django.db import models

# Create your models here.

STATUS_CHOICES = [('new', 'New'), ('in_progress', 'Processing'), ('done', 'Completed')]

class Article(models.Model):
    project = models.CharField(max_length=50, null=False, blank=False, verbose_name="Zagalovoc")
    author = models.CharField(max_length=50, verbose_name="Author", default="Unknown")
    content = models.TextField(max_length=3000, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name='Status')


    def __str__(self):
        return f"{self.pk}, {self.project}, {self.author}, {self.status}"


    class Meta:
        db_table = "articles"
        verbose_name = "Project"
        verbose_name_plural = "Projects"
