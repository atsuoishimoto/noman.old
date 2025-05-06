from django.shortcuts import render
from .models import NomanPage
from django.http import HttpResponseNotFound


# Create your views here.
def nomanpage(request, lang, name):
    """
    View function to render a Noman page.
    """
    if 0:
        # Fetch the Noman page from the database
        try:
            noman_page = NomanPage.objects.get(lang=lang, name=name)
        except NomanPage.DoesNotExist:
            raise HttpResponseNotFound

        # Render the page with the fetched data
        return render(request, "nomanpage.html", {"noman_page": noman_page})
    return render(request, "nomanpages/nomanpage.html")
