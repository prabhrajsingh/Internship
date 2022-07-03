from django.contrib import admin
from FEEDBACKS.models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)
