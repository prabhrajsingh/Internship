from django.shortcuts import render

# Create your views here.
def review_create_view(request):

    form = FeeForm(request.POST or None)
    context = {
                "form" : form
              }

    if (form.is_valid()):
        review_obj = form.save()
        context['form'] = ReviewForm()
        return redirect(review_obj.get_absolute_url())
        # context['object'] = review_obj
        # context['created'] = True

    return render(request, "reviews/create.html", context = context)