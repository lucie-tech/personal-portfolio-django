from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20, default="Intermediate")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    organization_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-start_date", "-id"]
        verbose_name_plural = "experience"

    def __str__(self):
        return f"{self.role} at {self.organization}"