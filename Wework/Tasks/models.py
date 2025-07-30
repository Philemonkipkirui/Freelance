from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField( max_length= 40)
    client_name = models.CharField(max_length= 20)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=6, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')
    status = models.CharField(null = True, blank = True, max_length = 20, choices = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),],
        default='pending')
    completed = models.BooleanField(null=True, blank = True, default=False)

    def __str__(self):
        return self.title