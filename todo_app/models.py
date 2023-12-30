from django.db import models
from django.urls import reverse
from django.utils import timezone

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class Tag(models.Model):
    value = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.value

class ToDoItem(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        WORKING = 'WORKING', 'Working'
        DONE = 'DONE', 'Done'
        OVERDUE = 'OVERDUE', 'Overdue'

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN
    )

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
