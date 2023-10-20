from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# Define a dictionary with monthly challenges.
monthly_challenges = {
    "january": "Start reading a book",
    "february": "Play football on phone",
    "march": "Start browsing well",
    "april": "Read a book",
    "may": "Start reading a book",
    "june": "Start reading a book",
    "july": "Start reading a book",
    "august": "Start reading a book",
}
def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month] )

        list_item += f'<li><a href="{month_path}"> {capitalize_month} </a></li>'
    response_data = f'<ul><h1>{list_item}</h1></ul>'
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    forward_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[forward_month])
    
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
        response_data = f'<h1>{challenges_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("not found at all ")

