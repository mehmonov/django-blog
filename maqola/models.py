from django.db import models
from django.utils import timezone
from users.models import UserProfile
from ckeditor.fields import RichTextField

class Maqola(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    content = RichTextField()

    created_at = models.DateTimeField(default=timezone.now)

    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    maqola = models.ForeignKey("Maqola", on_delete=models.CASCADE)

    vaqti = models.DateTimeField(default=timezone.now)

    adminReply = models.CharField(null=True, blank=True)
    comment = models.TextField()
    
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.maqola}"
    
class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    maqola = models.ForeignKey("Maqola", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.maqola}"

        
class Category(models.Model):
    name = models.CharField()

    def __str__(self):
        return f"{self.name}"