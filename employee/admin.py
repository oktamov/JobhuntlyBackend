from django.contrib import admin
from .models import Employee, Education, University, Experience, EmployeeSkill, Skill

admin.site.register(Employee)

admin.site.register(Education)
admin.site.register(University)
admin.site.register(Experience)
admin.site.register(EmployeeSkill)
admin.site.register(Skill)
