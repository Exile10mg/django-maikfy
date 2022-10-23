from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
  def thumbmail(self, object):
    return format_html(f'<img src="{object.photo.url}" style="border-radius: 50px"  width="40 "/>')
  thumbmail.short_description = 'Photo'
  list_display =  ('id', 'thumbmail' , 'first_name', 'last_name', 'designation', 'create_date')
  list_display_links = ('first_name', 'id', 'thumbmail')
  search_fields = ('first_name', 'last_name', 'designation')
  list_filter = ('designation', )
admin.site.register(Team, TeamAdmin)