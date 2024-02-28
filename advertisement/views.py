from django.http import HttpResponse
from django.views.decorators.http import require_GET
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from advertisement.forms import ReklamForm
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementSerializer


@login_required(login_url='/user/login')
def reklam_olustur(request):
    
    if request.method == 'POST':
        form = ReklamForm(request.POST, request.FILES)

        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.kampanya_creator = request.user 
            advertisement.save()

            # Add a success message
            messages.success(request, 'Reklam başarıyla kaydedildi/Advertisement was successfully created.')

            # Use reverse to dynamically generate the URL
            return redirect(reverse('advertisement:advertisement/reklam_olustur'))
    else:
 
        form = ReklamForm()

    return render(request, 'advertisement/reklam_olustur.html', {'form': form})

@login_required(login_url='/user/login')
def reklam_paneli(request):    
    return render(request, 'advertisement/reklam_paneli.html')  

@login_required(login_url='/user/login')
def hesap_ayarlari(request):    
    return render(request, 'advertisement/hesap_ayarlari.html')  

@login_required(login_url='/user/login')
def odemeler(request):    
    return render(request, 'advertisement/odemeler.html')  

@login_required(login_url='/user/login')
def fatura(request):    
    return render(request, 'advertisement/fatura.html')  

@login_required(login_url='/user/login')
def bakiye(request):    
    return render(request, 'advertisement/bakiye.html')  

@action(detail=True, methods=['get'])
def creator_advertisements(self, request, pk=None):
        # Get the advertisement object
        advertisement = self.get_object()
        
        # Get the creator associated with the advertisement
        creator = advertisement.kampanya_creator

        # Get all advertisements by the creator
        advertisements_by_creator = Advertisement.objects.filter(
            kampanya_creator=creator,
            is_active=True,
            is_deleted=False,
        )

        # Serialize the advertisements
        serialized_advertisements = AdvertisementSerializer(advertisements_by_creator, many=True).data

        return Response({
            "status": True,
            "message": "Advertisements retrieved successfully.",
            "data": serialized_advertisements
        })

@require_GET
def track_image_view(request, pk=None, image_field_name=None):
    # Get the advertisement object
    advertisement = Advertisement.objects.get(pk=pk)

    # Increment the view count for the specified image field
    advertisement.increment_views(image_field_name)

    # Serve the image file
    image_file = getattr(advertisement, image_field_name)
    response = HttpResponse(image_file.read(), content_type='image/jpeg')  # Adjust content type based on your image format
    response['Content-Disposition'] = 'inline; filename=' + image_file.name
    return response
