from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.URLField()
    github_url = models.URLField()
    facebook_url = models.URLField()

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    technologies = models.CharField(max_length=200)  # e.g., "Python, Django"
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon_url = models.URLField()

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    graduation_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certifications')
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    issue_date = models.DateField()
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title