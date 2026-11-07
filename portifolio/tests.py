from django.test import TestCase

from .models import Experience, Project, Skill


class PortfolioPageTests(TestCase):
    def test_homepage_renders_portfolio_sections(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Selected projects")
        self.assertContains(response, "Experience")
        self.assertContains(response, "Skills &amp; tools")

    def test_homepage_displays_project_links_skills_and_experience(self):
        project = Project.objects.create(
            title="Portfolio site",
            description="A site to share my work.",
            tech_stack="Django, Python",
            github_url="https://github.com/example/portfolio",
            live_url="https://example.com",
        )
        skill = Skill.objects.create(name="Python", level="Intermediate")
        experience = Experience.objects.create(
            role="Student",
            organization="University of Dodoma",
            start_date="2024-01-01",
            is_current=True,
            description="Studying software engineering.",
        )

        response = self.client.get("/")

        self.assertContains(response, project.title)
        self.assertContains(response, project.github_url)
        self.assertContains(response, project.live_url)
        self.assertContains(response, skill.name)
        self.assertContains(response, skill.level)
        self.assertContains(response, experience.role)
        self.assertContains(response, "Present")

    def test_about_page_renders(self):
        response = self.client.get("/about/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "University of Dodoma")
