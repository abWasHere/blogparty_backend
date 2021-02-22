from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=True)
    # user = models.ForeignKey("User", on_delete=models.CASCADE)
    user = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.title + " is added."


class Tag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
