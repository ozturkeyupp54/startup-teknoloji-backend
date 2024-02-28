from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from girisimci.models import Girisimci
from girisimci.forms import GirisimciForm

class GirisimciListView(View):
    template_name = 'girisimci_list.html'

    def get(self, request):
        girisimciler = Girisimci.objects.filter(is_active=True, is_deleted=False)
        return render(request, self.template_name, {'girisimciler': girisimciler})

class GirisimciCreateView(View):
    template_name = 'girisimci_create.html'

    def get(self, request):
        form = GirisimciForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GirisimciForm(request.POST)
        if form.is_valid():
            girisimci = form.save()
            return HttpResponse(f"Girisimci record successfully created. ID: {girisimci.id}")
        return render(request, self.template_name, {'form': form})
