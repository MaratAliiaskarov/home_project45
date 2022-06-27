from django.db import models

# Create your models here.

class Article(models.Model):
    project = models.CharField(max_length=50, null=False, blank=False, verbose_name="Zagalovoc")
    author = models.CharField(max_length=50, verbose_name="Author", default="Unknown")
    content = models.TextField(max_length=3000, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")


    def __str__(self):
        return f"{self.pk}, {self.project}, {self.author}"


    class Meta:
        db_table = "articles"
        verbose_name = "Statya"
        verbose_name_plural = "Statii"
