from django.contrib import admin

from Company.models import companymodel

# Register your models here.



class slugadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']


admin.site.register(companymodel,slugadmin)