from django.contrib import admin
from .models import UserProfile, Project, Skill, Education, Certification

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certification)