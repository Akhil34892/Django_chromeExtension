from django.db import models

class UserEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class ModalContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)  # For YouTube videos
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # For file uploads
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
