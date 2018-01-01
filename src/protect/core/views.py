from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from protect.core.models import Person


def landing(request):
    template_name = 'landing.html'
    person_list = Person.objects.filter(is_active="True")
    page = request.GET.get('page', 1)
    paginator = Paginator(person_list, 12)
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
    return render(request, template_name, {'persons': persons, 'active': 'inicio'})


def missing(request):
    template_name = 'landing.html'
    person_list = Person.objects.filter(is_active="True", type_publication="missing")
    page = request.GET.get('page', 1)
    paginator = Paginator(person_list, 12)
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
    return render(request, template_name, {'persons': persons, 'active': 'missing'})


def found(request):
    template_name = 'landing.html'
    person_list = Person.objects.filter(is_active="True", type_publication="found")
    page = request.GET.get('page', 1)
    paginator = Paginator(person_list, 12)
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
    return render(request, template_name, {'persons': persons, 'active': 'found'})


def detail_slug(request, slug):
    template_name = 'detail.html'
    person = Person.objects.get(is_active="True", slug=slug)
    return render(request, template_name, {'person': person})
