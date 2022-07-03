from django.contrib import admin
from FEEDBACKS.models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','suggestion']
    search_fields = ['id', 'suggestion']
    

admin.site.register(Feedback)
