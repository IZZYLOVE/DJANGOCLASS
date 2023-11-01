from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, world!")

from myapp.forms import InputeForm
def form_view(request):
    form = InputeForm()
    context = {"form": form}
    return render(request, "home.html", context)

from myapp.forms import LogForm # for the modelForm
def modelform_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST) # updates the form objects with the contents of Post inside the request object
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

from myapp.models import Menu # for the modelForm
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request, 'menu_card.html', newmenu_dict)