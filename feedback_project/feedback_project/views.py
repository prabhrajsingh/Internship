from lib2to3.refactor import get_all_fix_names
from urllib import response
from django.shortcuts import render
from django.template.loader import render_to_string
from FEEDBACKS.models import Feedback



def idea(request):
    #feedback_link = """<a href=https://youtu.be/dQw4w9WgXcQ>FEEDBACK LINK</a>"""
    return render(request, 'home_view.html')

def suggestion(request):
    return render(request,'create.html')

