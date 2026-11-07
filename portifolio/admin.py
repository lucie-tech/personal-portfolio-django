from django.contrib import admin
from .models import Experience, Project, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "github_url", "live_url")
    search_fields = ("title", "description", "tech_stack")
    ordering = ("-created",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "organization", "start_date", "end_date", "is_current")
    list_filter = ("is_current",)
    search_fields = ("role", "organization", "description")
    ordering = ("-start_date",)