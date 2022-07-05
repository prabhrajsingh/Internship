from cgitb import text
from django.shortcuts import render
from FEEDBACKS.models import Feedback


def idea(request):
    #feedback_link = """<a href=https://youtu.be/dQw4w9WgXcQ>FEEDBACK LINK</a>"""
    return render(request, 'home.html')