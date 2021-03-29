from django.contrib import admin
from .models import User,Keyword,Result
# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    class Meta:
        model=User
        fields=('title','description','user','keyword','date')
admin.site.register(User)
admin.site.register(Keyword)
admin.site.register(Result,ResultAdmin)
