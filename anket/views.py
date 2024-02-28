from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from anket.models import Anket, Soru, Cevap, Sonuc

class LoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

# Anket views
class AnketListView(ListView):
    model = Anket
    template_name = 'anket_list.html'

class AnketDetailView(DetailView):
    model = Anket
    template_name = 'anket_detail.html'

class AnketCreateView(CreateView):
    model = Anket
    fields = ['anket_baslik', 'aciklama', 'anket_baslik_resmi']
    template_name = 'anket_create.html'
    success_url = reverse_lazy('anket_list')

class AnketUpdateView(LoginRequiredMixin, UpdateView):
    model = Anket
    fields = ['baslik', 'aciklama']
    template_name = 'anket_update.html'
    success_url = reverse_lazy('anket_list')

class AnketDeleteView(LoginRequiredMixin, DeleteView):
    model = Anket
    template_name = 'anket_delete.html'
    success_url = reverse_lazy('anket_list')

# Soru views (nested under Anket views)
class SoruListView(LoginRequiredMixin, ListView):
    model = Soru
    template_name = 'soru_list.html'

    def get_queryset(self):
        # Filter questions by selected Anket (accessible through URL pattern)
        return Soru.objects.filter(anket=self.kwargs['pk'])

class SoruCreateView(LoginRequiredMixin, CreateView):
    model = Soru
    fields = ['icerik']
    template_name = 'soru_create.html'

    def form_valid(self, form):
        # Set Anket based on URL pattern
        form.instance.anket = Anket.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    success_url = reverse_lazy('anket_detail', kwargs={'pk': '<pk>'})  # Dynamic based on Anket pk

class SoruUpdateView(LoginRequiredMixin, UpdateView):
    model = Soru
    fields = ['icerik']
    template_name = 'soru_update.html'

    success_url = reverse_lazy('anket_detail', kwargs={'pk': '<pk>'})  # Dynamic based on Anket pk

class SoruDeleteView(LoginRequiredMixin, DeleteView):
    model = Soru
    template_name = 'soru_delete.html'

    success_url = reverse_lazy('anket_detail', kwargs={'pk': '<pk>'})  # Dynamic based on Anket pk

# Cevap views (nested under Soru views)
class CevapListView(LoginRequiredMixin, ListView):
    model = Cevap
    template_name = 'cevap_list.html'

    def get_queryset(self):
        # Filter answers by selected Soru (accessible through URL pattern)
        return Cevap.objects.filter(soru=self.kwargs['pk'])

# Sonuc views (nested under Anket views)
class SonucListView(LoginRequiredMixin, ListView):
    model = Sonuc
    template_name = 'sonuc_list.html'

    def get_queryset(self):
        # Filter results by selected Anket (accessible through URL pattern)
        return Sonuc.objects.filter(anket=self.kwargs['pk'])


# from django.shortcuts import render, redirect
# from anket.models import Anket, Soru
# from anket.forms import AnketOlusturForm, SoruEkleForm

# def anket_olustur(request):
#     if request.method == 'POST':
#         form = AnketOlusturForm(request.POST)
#         if form.is_valid():
#             baslik = form.cleaned_data['baslik']
#             aciklama = form.cleaned_data['aciklama']
#             user = request.user  # Bu kullanıcıyı login yapan kullanıcıya ayarlayın
            
#             anket = Anket.objects.create(
#                 user=user,
#                 baslik=baslik,
#                 aciklama=aciklama,
#             )
            
#             # Google Forms API ile anket oluşturup bilgileri kaydetme
#             form_id = anket.create_form(baslik, aciklama)
            
#             # Diğer işlemler...
            
#             return redirect('soru_ekle', anket_id=anket.id)
#     else:
#         form = AnketOlusturForm()
    
#     return render(request, 'anket/anket_olustur.html', {'form': form})

# def soru_ekle(request, anket_id):
#     anket = Anket.objects.get(id=anket_id)

#     if request.method == 'POST':
#         form = SoruEkleForm(request.POST)
#         if form.is_valid():
#             icerik = form.cleaned_data['icerik']
#             user = request.user  # Bu kullanıcıyı login yapan kullanıcıya ayarlayın

#             Soru.objects.create(
#                 user=user,
#                 anket=anket,
#                 icerik=icerik,
#             )
#             return redirect('soru_ekle', anket_id=anket_id)
#     else:
#         form = SoruEkleForm()

#     return render(request, 'anket/soru_ekle.html', {'form': form, 'anket': anket, 'forms': anket.list_google_forms()})


# from django.shortcuts import render, redirect
# from django.template.loader import render_to_string
# from django.http import HttpResponseRedirect
# from anket.models import Questionnaire, Question, Answer
# from .forms import AnswerForm
# from django.contrib import messages

# def index(request):
#     # Consider returning specific questionnaires or redirecting
#     all_questionnaires = Questionnaire.objects.all()
#     context = {'questionnaires': all_questionnaires}
#     return render(request, 'anket/index.html', context)

# def questionnaire_detail(request, questionnaire_id):
#     try:
#         questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
#         questions = Question.objects.filter(questionnaire=questionnaire)
#         # Add context variables as needed (e.g., success/error messages)
#         context = {'questionnaire': questionnaire, 'questions': questions}
#         return render(request, 'anket/questionnaire.html', context)
#     except Questionnaire.DoesNotExist:
#         messages.error(request, "Questionnaire not found.")
#         return redirect('main:index')

# def calculate(request):
#     if request.method == 'POST':
#         # Implement calculation logic here
#         # Redirect to appropriate page based on results
#         pass
#     else:
#         return redirect('main:index')

# def answerpage(request, questionnaire_pk):
#     questionnaire = Questionnaire.objects.get(pk=questionnaire_pk)
#     questions = Question.objects.filter(questionnaire=questionnaire)

#     if request.method == 'POST':
#         answer_formset = AnswerFormSet(request.POST)
#         if answer_formset.is_valid():
#             for form in answer_formset:
#                 if form.is_valid():
#                     # Handle saving, potentially using form.instance.save()
#                     pass
#             # Redirect to success page
#             return redirect('main:success')
#         else:
#             # Handle errors, potentially re-rendering form with populated errors
#             pass
#     else:
#         answer_formset = AnswerFormSet()

#     context = {
#         'questionnaire': questionnaire,
#         'questions': questions,
#         'answer_formset': answer_formset,
#     }
#     return render(request, 'anket/questionnaire.html', context)