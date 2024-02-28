# views.py
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import F
from django.utils import timezone
from django.shortcuts import render
from post.models import Post
from advertisement.models import Advertisement
from alt_reklam_alani.models import FooterReklami


def girisim_ve_yatirim(request):
    # Add your logic for 'girisim_ve_yatirim' view here
    return render(request, 'navbar-top/girisim_ve_yatirim.html')  # Update with your actual template name

def reklam_ve_sponsorluk(request):
    # Add your logic for 'reklam_ve_sponsorluk' view here
    return render(request, 'navbar-top/reklam_ve_sponsorluk.html')  # Update with your actual template name

def anket(request):
    # Add your logic for 'anket' view here
    return render(request, 'navbar-top/anket.html')  # Update with your actual template name

def kariyer(request):
    # Add your logic for 'kariyer' view here
    return render(request, 'navbar-top/kariyer.html')  # Update with your actual template name

def kunye(request):
    # Add your logic for 'kunye' view here
    return render(request, 'navbar-top/kunye.html')  # Update with your actual template name

def iletisim(request):
    # Add your logic for 'iletisim' view here
    return render(request, 'navbar-top/iletisim.html')  # Update with your actual template name
    
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch the Post objects
        post_list = Post.objects.filter(yayimlanma_durumu='Yayinda')
        paginator = Paginator(post_list, 20)  # Show 20 posts per page

        page = self.request.GET.get('page')
        posts = paginator.get_page(page)
        
        girisimcilik_posts = Post.objects.filter(category__name="GIRISIMCILIK", yayimlanma_durumu='Yayinda')
        context['girisimcilik_posts'] = girisimcilik_posts

        # Fetch the Advertisement object you want to display
        try:
            advertisement = Advertisement.objects.filter(is_active=True, is_deleted=False).first()
        except Advertisement.DoesNotExist:
            advertisement = None
        
        context['posts'] = posts
        
        # Get the advertisements that are not deleted, have not reached their view limit,
        # kampanya_baslangic_tarihi is after today, and kampanya_baslangic_tarihi is not in the past
        current_date = timezone.now().date()
        active_ads = Advertisement.objects.filter(
            is_active=True,
            is_deleted=False,
            max_views_per_image__gt=F('advertisement_ust_resmi_views'),
            kampanya_baslangic_tarihi__lte=current_date
        )

        # Exclude advertisements that have reached their view limit
        active_ads = active_ads.exclude(id__in=context.get('viewed_ad_ids', []))

        # Now, fetch the next advertisement to display
        try:
            advertisement = active_ads.order_by('?').distinct().first()

            if advertisement:
                # Increment the views for the selected advertisement
                advertisement.increment_views('advertisement_ust_resmi')

                # Add the advertisement ID to the viewed_ad_ids in the context
                context.setdefault('viewed_ad_ids', []).append(advertisement.id)
        except Advertisement.DoesNotExist:
            advertisement = None
        context['advertisement'] = advertisement

        # context['advertisement_ust'] = Advertisement.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Üst').order_by('?').distinct().first()
        context['advertisement_alt'] = FooterReklami.objects.filter(is_active=True, is_deleted=False, reklam_gosterim_yeri='Alt').order_by('?').distinct().first()

        return context


