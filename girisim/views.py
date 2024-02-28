from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.db.models import Q
from girisim.models import Girisim, GirisimHaberleri, GirisimGelismelerHedefler, GirisiminYatirimTurlari
from girisim.forms import GirisimForm, GirisimHaberleriForm, GirisimGelismelerHedeflerForm, GirisiminYatirimTurlariForm




class GirisimListView(ListView):
    model = Girisim
    paginate_by = 8
    template_name = 'girisim/girisim_list.html'
    context_object_name = 'girisimler'
    ordering = ['-pk']

    def get_queryset(self):
        queryset = Girisim.objects.filter(is_active=True, is_deleted=False).order_by('-pk')

        # 'order' query parameter
        order_param = self.request.GET.get('order')

        if order_param == 'alphabetical':
            queryset = queryset.order_by('girisim_adi')
        elif order_param == 'createdAt':
            queryset = queryset.order_by('created_at')
        elif order_param == 'startDate':
            queryset = queryset.order_by('girisim_kurulus_tarihi')

        return queryset

class GirisimDetailView(DetailView):
    model = Girisim
    template_name = 'girisim/girisim_detail.html'
    context_object_name = 'girisim'

def girisim_create(request):
    if request.method == 'POST':
        form = GirisimForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim başarıyla oluşturuldu.')
            return redirect('girisim_list')
    else:
        form = GirisimForm()
    return render(request, 'girisim/girisim_form.html', {'form': form})

def girisim_update(request, pk):
    instance = get_object_or_404(Girisim, pk=pk)
    if request.method == 'POST':
        form = GirisimForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim başarıyla güncellendi.')
            return redirect('girisim_list')
    else:
        form = GirisimForm(instance=instance)
    return render(request, 'girisim/girisim_form.html', {'form': form})

def girisim_delete(request, pk):
    instance = get_object_or_404(Girisim, pk=pk)
    instance.delete()
    messages.success(request, 'Girişim başarıyla silindi.')
    return redirect('girisim_list')


class GirisimSearchView(ListView):
    model = Girisim
    template_name = 'girisim/girisim_search.html'
    context_object_name = 'girisimler'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Girisim.objects.filter(Q(girisim_adi__icontains=query)).order_by('-pk')
        else:
            return Girisim.objects.all().order_by('-pk')

##################################################################################

class GirisimHaberleriListView(ListView):
    model = GirisimHaberleri
    paginate_by = 8
    template_name = 'girisim/girisimhaberleri_list.html'  # Change 'your_template_path' to your actual path
    context_object_name = 'girisim_haberleri'
    ordering = ['-pk']

    def get_queryset(self):
        return GirisimHaberleri.objects.filter(is_active=True, is_deleted=False).order_by('-pk')

class GirisimHaberleriDetailView(DetailView):
    model = GirisimHaberleri
    template_name = 'girisim/girisimhaberleri_detail.html'  # Change 'your_template_path' to your actual path
    context_object_name = 'girisim_haber'

def girisimhaberleri_create(request):
    if request.method == 'POST':
        form = GirisimHaberleriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim haberi başarıyla oluşturuldu.')
            return redirect('girisimhaberleri_list')
    else:
        form = GirisimHaberleriForm()
    return render(request, 'girisim/girisimhaberleri_form.html', {'form': form})  # Change 'your_template_path' to your actual path

def girisimhaberleri_update(request, pk):
    instance = get_object_or_404(GirisimHaberleri, pk=pk)
    if request.method == 'POST':
        form = GirisimHaberleriForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim haberi başarıyla güncellendi.')
            return redirect('girisimhaberleri_list')
    else:
        form = GirisimHaberleriForm(instance=instance)
    return render(request, 'girisim/girisimhaberleri_form.html', {'form': form})  # Change 'your_template_path' to your actual path

def girisimhaberleri_delete(request, pk):
    instance = get_object_or_404(GirisimHaberleri, pk=pk)
    instance.delete()
    messages.success(request, 'Girişim haberi başarıyla silindi.')
    return redirect('girisimhaberleri_list')

#######################################################################
class GirisimGelismelerHedeflerListView(ListView):
    model = GirisimGelismelerHedefler
    paginate_by = 8
    template_name = 'girisim/girisimgelismelerhedefler_list.html'  # Change 'your_template_path' to your actual path
    context_object_name = 'gelismeler_hedefler'
    ordering = ['-pk']

    def get_queryset(self):
        return GirisimGelismelerHedefler.objects.filter(is_active=True, is_deleted=False).order_by('-pk')

class GirisimGelismelerHedeflerDetailView(DetailView):
    model = GirisimGelismelerHedefler
    template_name = 'girisim/girisimgelismelerhedefler_detail.html'  # Change 'your_template_path' to your actual path
    context_object_name = 'gelisme_hedef'

def girisimgelismelerhedefler_create(request):
    if request.method == 'POST':
        form = GirisimGelismelerHedeflerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim Gelisme veya Hedef başarıyla oluşturuldu.')
            return redirect('girisimgelismelerhedefler_list')
    else:
        form = GirisimGelismelerHedeflerForm()
    return render(request, 'girisim/girisimgelismelerhedefler_form.html', {'form': form})  # Change 'your_template_path' to your actual path

def girisimgelismelerhedefler_update(request, pk):
    instance = get_object_or_404(GirisimGelismelerHedefler, pk=pk)
    if request.method == 'POST':
        form = GirisimGelismelerHedeflerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Girişim Gelisme veya Hedef başarıyla güncellendi.')
            return redirect('girisimgelismelerhedefler_list')
    else:
        form = GirisimGelismelerHedeflerForm(instance=instance)
    return render(request, 'girisim/girisimgelismelerhedefler_form.html', {'form': form})  # Change 'your_template_path' to your actual path

def girisimgelismelerhedefler_delete(request, pk):
    instance = get_object_or_404(GirisimGelismelerHedefler, pk=pk)
    instance.delete()
    messages.success(request, 'Girişim Gelisme veya Hedef başarıyla silindi.')
    return redirect('girisimgelismelerhedefler_list')

###################################################################################


@method_decorator(login_required, name='dispatch')
class GirisiminYatirimTurlariListView(ListView):
    model = GirisiminYatirimTurlari
    template_name = 'girisiminyatirimturlari/girisiminyatirimturlari_list.html'  # Şablonunuzu oluşturun
    context_object_name = 'yatirimlar'
    paginate_by = 10  # Sayfada gösterilecek öğe sayısı

    def get_queryset(self):
        return GirisiminYatirimTurlari.objects.filter(is_active=True, is_deleted=False).order_by('-pk')

@method_decorator(login_required, name='dispatch')
class GirisiminYatirimTurlariDetailView(DetailView):
    model = GirisiminYatirimTurlari
    template_name = 'girisiminyatirimturlari/girisiminyatirimturlari_detail.html'  # Şablonunuzu oluşturun
    context_object_name = 'yatirim'

@method_decorator(login_required, name='dispatch')
class GirisiminYatirimTurlariCreateView(CreateView):
    model = GirisiminYatirimTurlari
    form_class = GirisiminYatirimTurlariForm  # Form sınıfınızı ekleyin
    template_name = 'girisiminyatirimturlari/girisiminyatirimturlari_form.html'  # Şablonunuzu oluşturun

    def form_valid(self, form):
        form.instance.girisimci = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Yatırım başarıyla oluşturuldu.')
        return reverse_lazy('yatirimlar_list')

@method_decorator(login_required, name='dispatch')
class GirisiminYatirimTurlariUpdateView(UpdateView):
    model = GirisiminYatirimTurlari
    form_class = GirisiminYatirimTurlariForm  # Form sınıfınızı ekleyin
    template_name = 'girisiminyatirimturlari/girisiminyatirimturlari_form.html'  # Şablonunuzu oluşturun

    def form_valid(self, form):
        form.instance.girisimci = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Yatırım başarıyla güncellendi.')
        return reverse_lazy('yatirimlar_list')

@method_decorator(login_required, name='dispatch')
class GirisiminYatirimTurlariDeleteView(DeleteView):
    model = GirisiminYatirimTurlari
    template_name = 'girisiminyatirimturlari/girisiminyatirimturlari_confirm_delete.html'  # Şablonunuzu oluşturun
    success_url = reverse_lazy('yatirimlar_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.girisimci == self.request.user:
            messages.success(self.request, 'Yatırım başarıyla silindi.')
            self.object.delete()
            return redirect(self.get_success_url())
        else:
            return HttpResponseForbidden('Bu işlem için izniniz yok.')
