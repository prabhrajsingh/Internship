from django.contrib import admin
from FEEDBACKS.models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','comment_type', 'timestamp', 'updated']
    search_fields = ['id', 'comment_type', 'timestamp']
    

admin.site.register(Feedback, FeedbackAdmin)
