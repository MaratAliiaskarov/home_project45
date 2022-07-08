from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        abstract = True



STATUS_CHOICES = [('new', 'New'), ('in_progress', 'Processing'), ('done', 'Completed')]

class Article(BaseModel):
    project = models.CharField(max_length=50, null=False, blank=False, verbose_name="Zagalovoc")
    author = models.CharField(max_length=50, verbose_name="Author", default="Unknown")
    content = models.TextField(max_length=3000, verbose_name="Content")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name='Status')


    def __str__(self):
        return f"{self.pk}, {self.project}, {self.author}, {self.status}"


    class Meta:
        db_table = "articles"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Comment(BaseModel):
    text = models.TextField(max_length=400, verbose_name="Comments")
    author = models.CharField(max_length=40, null=True, blank=True, default="Anonim", verbose_name="Project")
    article = models.ForeignKey("webapp.Article", on_delete=models.CASCADE, related_name="comments", verbose_name="Project")


    def __str__(self):
        return f"{self.pk}, {self.text}, {self.author}"


    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"