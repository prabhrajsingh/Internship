from tkinter.tix import Tree
from django.shortcuts import redirect, render
from .forms import FeedbackForm
from .models import Feedback


# Create your views here.
def enter_suggestion(request):
    dictionary = {}
    if request.method == "POST":
        comment_type =  request.POST.get('comment_type')
        suggestion =  request.POST.get('suggestion')
        feedback_obj = Feedback.objects.create(comment_type = comment_type, suggestion = suggestion )
        dictionary['object'] = feedback_obj
        dictionary['created'] = True

    return render(request, "FEEDBACKS/create.html", context = dictionary)
