from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from alt_reklam_alani.forms import ReklamForm
from alt_reklam_alani.models import FooterReklami


@login_required(login_url='/user/login')
def footer_reklami_olustur(request):
    
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



@require_GET
def track_image_view(request, pk=None, image_field_name=None):
    # Get the advertisement object
    advertisement = FooterReklami.objects.get(pk=pk)

    # Increment the view count for the specified image field
    advertisement.increment_views(image_field_name)

    # Serve the image file
    image_file = getattr(advertisement, image_field_name)
    response = HttpResponse(image_file.read(), content_type='image/jpeg')  # Adjust content type based on your image format
    response['Content-Disposition'] = 'inline; filename=' + image_file.name
    return response
