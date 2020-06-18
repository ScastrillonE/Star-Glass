from django.contrib import admin
from .models import Project,Service,Testimonial
# Register your models here.


admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Testimonial)